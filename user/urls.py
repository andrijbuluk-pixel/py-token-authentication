from rest_framework.urls import path

from user.views import (
    CreateUser,
    CreateTokenView
)

urlpatterns = [
    path("register/", CreateUser.as_view(), name="create_user"),
    path("login/", CreateTokenView.as_view(), name="obtain_pass"),
]

app_name = "user"
