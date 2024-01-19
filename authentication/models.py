from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Модель пользователя.
    Реализована путем подмены основного пользователя Django.
    Сделано так для исключения создания промежуточных таблиц
    """
    MALE = 'm'
    FEMALE = 'w'
    SEX = [(MALE, 'Male'), (FEMALE, 'Female')]
    sex = models.CharField(max_length=1, choices=SEX, default=MALE)
    birthday = models.DateField(null=True)
