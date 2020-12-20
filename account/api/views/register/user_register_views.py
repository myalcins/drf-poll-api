from rest_framework.generics import CreateAPIView
from account.models import User
from .user_register_serializers import UserRegisterSerializer


class UserRegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
