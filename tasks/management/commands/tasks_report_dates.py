#команда выводить невыполненные задачи за последние X дней (5 по умолчанию)
# coding: utf-8
from django.core.management import BaseCommand
from datetime import datetime, timezone
from tasks.models import TodoItem

class Command(BaseCommand): #создаем класс Command наследуемый от BaseCommand
    help = u"Display not yet completed tasks' dates" #подсказка что делает команда

    def add_arguments(self, parser): #определяем дополнительные аргументы, перегружая метод add_arguments
        parser.add_argument('--warning-days', dest='warn_days', type=int, default=3)

    def handle(self, *args, **options): #описываем суть команды
        now = datetime.now(timezone.utc)
        for t in TodoItem.objects.filter(is_completed=False):
            if (now - t.created).days >= options['warn_days']:
                print("Старая задача:", t, t.created)