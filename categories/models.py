from django.db import models

from authentication.models import User


class Category(models.Model):
    """Модель Категорий"""
    TYPE_DEFAULT = 'default'
    TYPE_USER = 'user'
    TYPE = [(TYPE_DEFAULT, 'default'), (TYPE_USER, 'user')]
    title = models.CharField(max_length=200, null=True)
    color = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, choices=TYPE, default=TYPE_USER)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
