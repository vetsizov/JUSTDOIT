from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(blank=True, null=True)
    #avatar = models.ImageField(upload_to="user_avatars/%Y/%m/%d", default='user_avatars/noava.jpg', blank=True, null=True)

    def __str__(self):
        return "Профиль пользователя %s" % self.user.username