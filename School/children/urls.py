from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("activate/", views.activate, name="activate_student_account"),
    path("homework_page/", views.activate, name="homework_page"),
    path("login/", views.login_, name="login"),

]