from rest_framework import serializers

from authentication.models import User


class UserDetailViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    '''
    Вызываем метод create для переопределения пароля в хешированном виде
    '''

    def create(self, validate_data):
        user = super().create(validate_data)
        user.set_password(user.password)
        user.save()

        return user
