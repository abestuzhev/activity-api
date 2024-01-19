from rest_framework import serializers

from categories.models import Category


class CategorySerialazer(serializers.ModelSerializer):
    user = serializers.IntegerField(required=False)

    class Meta:
        model = Category
        fields = "__all__"
