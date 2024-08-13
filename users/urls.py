from django.urls import path
from . import views

urlpatterns = [
    path('signUp', views.sign_up, name="register"),
    path('login', views.login, name="login"),
]


