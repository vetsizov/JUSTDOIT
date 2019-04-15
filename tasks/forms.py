from django import forms
from tasks.models import TodoItem


class AddTaskForm(forms.Form):
    description = forms.CharField(max_length=64, label="")

'''Чтобы создать форму из модели, надо создать класс, наследующийся от django.forms.ModelForm
и ему в Meta указать модель, на базе которой будет строиться форма.
В Meta ещё указываются поля, которые эта форма заполняет. Мы оставим только description.'''
class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ("description", "priority")
        labels = {"description": "Описание", "priority": ""}

class TodoItemExportForm(forms.Form):
    prio_high = forms.BooleanField(
        label="высокая важность", initial=True, required=False
    )
    prio_med = forms.BooleanField(
        label="средней важности", initial=True, required=False
    )
    prio_low = forms.BooleanField(
        label="низкой важности", initial=False, required=False
    )