
from django.db import models
from authentication.models import User
from categories.models import Category


class Task(models.Model):
    """Модель Задачи"""
    title = models.CharField(max_length=200, null=True)
    text = models.CharField(max_length=2000, null=True)
    created = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)
    isImportant = models.BooleanField(default=False, null=True)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    categories = models.ManyToManyField(Category, default=1)

    def __str__(self):
        return self.text