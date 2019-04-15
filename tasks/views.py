'''views.py описывает основную логику работы с этим приложениям,
по идее здесь должны быть все обработчики http запросов, которые обрабатывают их и возвращают ответ'''
from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.models import TodoItem
from tasks.forms import AddTaskForm, TodoItemForm, TodoItemExportForm
from django.views import View
from django.views.generic import ListView
from django.urls import reverse #нужно чтобы использовать имена путей вместо полного пути
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.mail import send_mail #функция для отправки почты, использует настройки из settings
from django.conf import settings

from django.contrib import messages #для отправки сообщений в шаблон base.html

from django.db.models import Q # Объект Q используют, когда нужна какая-то более-менее сложная бинарная логика

from datetime import datetime as dt
a = dt.now().hour
if a >= 6 and a <= 11:
    vremya_s = 'Кстати, какой там у нас сейчас час? - ' + str(a) + '. Доброе утро! Пей кофе и принимайся за дела!'
    fcolor = 'IndianRed'
elif a >= 12 and a <= 17:
    vremya_s = 'Кстати, какой там у нас сейчас час? - ' + str(a) + '. Добрый день! Самое время сделать все дела!'
    fcolor = 'SpringGreen'
elif a >= 18 and a <= 24:
    vremya_s = 'Кстати, какой там у нас сейчас час? - ' + str(a) + '. Добрый вечер! Не ложись спать пока не выполнишь все дела!'
    fcolor = 'MediumAquamarine'
else:
    vremya_s = 'Кстати, какой там у нас сейчас час? - ' + str(a) + '. Доброй ночи! Спать некогда, делай дела!'
    fcolor = 'DarkSlateGray'


@login_required
def index(request):
    return HttpResponse("Функция index возвращает это сообщение с помощтю HttpResponse в ответ на request по адресу /tasks")

class TaskListView(LoginRequiredMixin, ListView):
    model = TodoItem
    context_object_name = "tasks"
    template_name = "tasks/list.html"

    def get_queryset(self):
        u = self.request.user
        qs = super().get_queryset()
        return qs.filter(owner=u)

    def get_context_data(self, *args, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context['vremya_s'] = vremya_s
        context['fcolor'] = fcolor
        return context

class TaskDetailsView(DetailView): #наследуется из DetailView. Получает объект {{ object }} и засовывает его в шаблон
    model = TodoItem
    template_name = 'tasks/details.html'

class TaskCreateView(View): #создаем класс, наследуемый из View
    def my_render(self, request, form):
        return render(request, "tasks/create.html", {"form": form})

    def post(self, request, *args, **kwargs): #функция ответа при запросе HTTP POST
        form = TodoItemForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.owner = request.user
            new_task.save()
            messages.success(request, 'задача добавлена')
            return redirect(reverse("tasks:list"))

        return self.my_render(request, form)

    def get(self, request, *args, **kwargs): #функция ответа при запросе HTTP GET
        form = TodoItemForm()
        return self.my_render(request, form)



def complete_task(request, uid): # path('complete/<int:uid>', views.complete_task, name='complete')
    t = TodoItem.objects.get(id=uid)
    t.is_completed = True
    t.save()
    messages.success(request, "задача выполнена")
    return redirect(reverse("tasks:list"))

def delete_task(request, uid): # path('delete/<int:uid>', views.delete_task, name='delete')
    t = TodoItem.objects.get(id=uid)
    t.delete()
    messages.success(request, "задача удалена") # выводим сообщение в шаблон base.html
    return redirect(reverse("tasks:list"))

class TaskEditView(LoginRequiredMixin, View): # редактирование задачи
    def post(self, request, pk, *args, **kwargs):
        t = TodoItem.objects.get(id=pk)
        form = TodoItemForm(request.POST, instance=t)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.owner = request.user
            new_task.save()
            messages.success(request, 'задача изменена')
            return redirect(reverse("tasks:list"))

        return render(request, "tasks/edit.html", {"form": form, "task": t})

    def get(self, request, pk, *args, **kwargs):
        t = TodoItem.objects.get(id=pk)
        form = TodoItemForm(instance=t)
        return render(request, "tasks/edit.html", {"form": form, "task": t})

#send_mail("Привет от django", "Письмо отправленное из приложения", settings.EMAIL_HOST_USER, ["v.sizov@enesi.ru"], fail_silently=False)

class TaskExportView(LoginRequiredMixin, View):
    def generate_body(self, user, priorities):
        q = Q()
        if priorities["prio_high"]:
            q = q | Q(priority=TodoItem.PRIORITY_HIGH)
        if priorities["prio_med"]:
            q = q | Q(priority=TodoItem.PRIORITY_MEDIUM)
        if priorities["prio_low"]:
            q = q | Q(priority=TodoItem.PRIORITY_LOW)
        tasks = TodoItem.objects.filter(owner=user).filter(q).all()

        body = "Ваши задачи и приоритеты:\n"
        for t in list(tasks):
            if t.is_completed:
                body += f"[x] {t.description} ({t.get_priority_display()})\n"
            else:
                body += f"[ ] {t.description} ({t.get_priority_display()})\n"

        return body

    def post(self, request, *args, **kwargs):
        form = TodoItemExportForm(request.POST)
        if form.is_valid():
            email = request.user.email
            body = self.generate_body(request.user, form.cleaned_data)
            send_mail("Задачи", body, settings.EMAIL_HOST_USER, [email])
            messages.success(
                request, "Задачи были отправлены на почту %s" % email)
        else:
            messages.error(request, "Что-то пошло не так, попробуйте ещё раз")
        return redirect(reverse("tasks:list"))

    def get(self, request, *args, **kwargs):
        form = TodoItemExportForm()
        return render(request, "tasks/export.html", {"form": form})

class TaskListViewSort(LoginRequiredMixin, ListView):
    model = TodoItem
    context_object_name = "tasks"
    template_name = "tasks/list.html"

    def get_queryset(self):
        u = self.request.user
        qs = super().get_queryset().order_by('priority')
        return qs.filter(owner=u)

    def get_context_data(self, *args, **kwargs):
        context = super(TaskListViewSort, self).get_context_data(**kwargs)
        context['vremya_s'] = vremya_s
        context['fcolor'] = fcolor
        return context