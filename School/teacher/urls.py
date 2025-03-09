from django.urls import path
from . import views

urlpatterns = [
    path("home", views.teacher_home, name='teacher_home'),
]