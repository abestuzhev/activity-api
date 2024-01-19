from rest_framework.generics import CreateAPIView, RetrieveAPIView

from authentication.models import User
from authentication.serializers import UserCreateSerializer, UserDetailViewSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailViewSerializer


class UserCreateView(CreateAPIView):
    modal = User
    serializer_class = UserCreateSerializer
