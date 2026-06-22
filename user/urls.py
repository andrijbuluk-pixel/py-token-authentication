from rest_framework.urls import path
from user.views import CreateUser


urlpatterns = [
    path("register/", CreateUser.as_view(), name="create_user"),
]

app_name = "user"