from django.db import models


class User(models.Model):
    email = models.EmailField('Email', max_length=256, unique=True)
    password = models.TextField('Пароль', max_length=14)
    name = models.TextField('Имя и фамилия', max_length=256)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
