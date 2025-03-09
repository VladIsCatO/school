from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("teacher_check/", views.teacher_check, name='teacher_check'),
    path("login/", views.login, name='login'),
]