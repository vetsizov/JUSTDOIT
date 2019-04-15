'''models.py описывает схемы базы данных для этого приложения'''

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class TodoItem(models.Model):
    PRIORITY_HIGH = 1
    PRIORITY_MEDIUM = 2
    PRIORITY_LOW = 3

    PRIORITY_CHOICES = [
        (PRIORITY_HIGH, "Высокий приоритет"),
        (PRIORITY_MEDIUM, "Средний приоритет"),
        (PRIORITY_LOW, "Низкий приоритет"),
    ]

    description = models.CharField(max_length=64)
    is_completed = models.BooleanField("выполнено", default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey( # владелец задачи
        User,
        on_delete=models.CASCADE, # при удалении пользователя удалятся и задачи
        related_name='tasks')
    priority = models.IntegerField( # приоритет задачи
        "Приоритет",
        choices=PRIORITY_CHOICES,
        default=PRIORITY_MEDIUM)

    def __str__(self):
        return self.description.lower()

#даем django понять, что одно из этих полей будет использовано для сортировки.
#Мы задаем порядок сортировки в поле ordering в специальном подклассе Meta.
    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self): #добавляем в админку кнопку "view on site"
        return reverse("tasks:details", args=[self.pk])
