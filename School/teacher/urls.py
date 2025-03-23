from django.urls import path
from . import views

urlpatterns = [
    path("", views.teacher_home, name='teacher_home'),
    path("teacher_check/", views.teacher_check, name='teacher_check'),
    path("register/", views.register_, name='register'),
    path("login/", views.login_, name='login'),
    path("group/", views.group, name="group"),
    path("schedule/", views.schedule_create, name="schedule_create"),
]