from rest_framework import generics

from user.serializers import UserSerializer


class CreateUser(generics.CreateAPIView):
    generic_serializer_class = UserSerializer
