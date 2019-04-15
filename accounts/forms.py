from django import forms
from django.contrib.auth.models import User
from accounts.models import Profile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) #виджет для ввода пароля

'''
В форме два поля для пароля. Это сделано, чтобы реализовать паттерн «введите пароль два раза».
Мы ограничиваем в этой форме поля, спрашивая у пользователя только username, имя и почту.
За совпадение паролей отвечает функция clean_password2.
'''
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "first_name", "email")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Пароли не совпадают")
        return cd["password2"]

class UserEditForm(forms.ModelForm): # форма для пользователя
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class ProfileEditForm(forms.ModelForm): # форма для профиля
    class Meta:
        model = Profile
        #fields = ("birthdate", "avatar")
        fields = ('birthdate',)