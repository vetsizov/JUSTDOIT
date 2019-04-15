from accounts.models import Profile
from django.contrib import admin

# чтобы редактировать профайл из админки
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin): # определяем класс, регистрируем его как админку для модели Profile и указываем, какие поля отображать
    #list_display = ["user", "birthdate", "avatar"]
    list_display = ["user", "birthdate"]