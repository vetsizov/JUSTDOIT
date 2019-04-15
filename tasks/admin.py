'''admin.py определяет, что и как можно сделать с сущностями приложения в контрольной панели администратора'''
from django.contrib import admin

# Register your models here.

from tasks.models import TodoItem

@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('description', 'is_completed', 'created')