from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("activate/", views.activate, name="activate_student_account"),

]