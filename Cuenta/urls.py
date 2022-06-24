from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
     path("login/", views.login_request, name = "login"),
     path("register/", views.register, name ="register"),
]
 