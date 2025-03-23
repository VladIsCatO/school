from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("login/", views.login, name='login'),
    path("add_teacher/", views.add_teacher, name='add_teacher'),
    path("add_group/", views.add_group, name='add_group'),
    path('associate_teacher/', views.associate_teacher, name="associate_teacher")
]