#команда для загрузки задач из файла в базу приложения
# coding: utf-8
from django.core.management import BaseCommand
from datetime import datetime, timezone
from tasks.models import TodoItem

class Command(BaseCommand):
	help = u"Read tasks from file (one line = one task) and save them to db"

	def add_arguments(self, parser):
		parser.add_argument('--file', dest='input_file', type=str) #аргумент --file <имя файла> должна быть строка

	def handle(self, *args, **options):
		file = open(options['input_file'], "r", encoding="utf-8") #открываем файл с именем <имя файла> переданным как аргумент команды
		temp = file.read().splitlines() #построчно читаем файл и заносим каждую строку в список
		for i in temp: #для каждого элемента списка создаем в базе новую запись с атрибутом description = строка из файла
			t = TodoItem(description=i)
			t.save()
		file.close()
		print('Файл ' + str(options['input_file']) + ' прочитан')
		print('В БД добавлены следующие задачи: ' + str(temp))
