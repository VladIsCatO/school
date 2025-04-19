from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, User
from base.models import Group, Teacher, Teacher_mails, Manager


# class Lesson(models.Model):
#     Headline = models.CharField(max_length=500)
#     subject = models.CharField(max_length=50)
#     date =models.DateTimeField(null=True)
#     homework = models.ManyToManyField('Homework')







    


class Student_mails(models.Model):
    email = models.EmailField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    code = models.CharField(max_length=50, null=True)