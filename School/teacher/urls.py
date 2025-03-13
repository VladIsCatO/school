from django.urls import path
from . import views

urlpatterns = [
    path("home", views.teacher_home, name='teacher_home'),
    path("teacher_check/", views.teacher_check, name='teacher_check'),
    path("login/", views.login_, name='login'),
]