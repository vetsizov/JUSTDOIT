# Generated by Django 2.1.5 on 2019-04-13 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190413_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='user_avatars/noava.jpg', null=True, upload_to='user_avatars/%Y/%m/%d'),
        ),
    ]