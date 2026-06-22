from rest_framework import generics

from user.serializers import UserSerializer


class CreateUser(generics.CreateAPIView):
    serializer_class = UserSerializer
