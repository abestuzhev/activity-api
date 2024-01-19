from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from categories.models import Category
from categories.serializers import CategorySerialazer


class CategoriesViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerialazer
