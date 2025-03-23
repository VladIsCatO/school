from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, User

class Break(models.Model):
    time = models.TimeField()
class Schedule_lesson(models.Model):
    subject = models.CharField(max_length=50)
    time = models.TimeField()
    
class Day(models.Model):
    day = models.DateField()
    lesson = models.ManyToManyField(Schedule_lesson)
    breaks = models.ManyToManyField(Break)

class schedule(models.Model):
    day = models.ManyToManyField(Day)

class Group(models.Model):
    name = models.CharField(max_length=100)
    schedule = models.ForeignKey(schedule, on_delete=models.CASCADE, null=True)

class Course(models.Model):
    name = models.CharField(max_length=100)
    groups = models.ManyToManyField(Group)

class Teacher(models.Model):  # Teachers
    groups = models.ManyToManyField(Group)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)

class Manager(models.Model):  # Manager creates teacher's account and group adds students to groups
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)



class Teacher_mails(models.Model):
    email = models.EmailField(max_length=100)
