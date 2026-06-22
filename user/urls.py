from django.contrib.auth.views import LogoutView
from rest_framework.urls import path

from user.views import (
    CreateUser,
    CreateTokenView,
    ManagerUserView,
)

urlpatterns = [
    path("register/", CreateUser.as_view(), name="create_user"),
    path("login/", CreateTokenView.as_view(), name="obtain_pass"),
    path("me/", ManagerUserView.as_view(), name="check_user_me"),
]

app_name = "user"
