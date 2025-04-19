from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, User


class Schedule_lesson(models.Model):
    subject = models.CharField(max_length=50)
    lesson_number = models.CharField(max_length=50)
    
class Day(models.Model):
    day = models.CharField(max_length=50)
    lesson = models.ManyToManyField(Schedule_lesson)


class schedule(models.Model):
    day = models.ManyToManyField(Day)

class Grade(models.Model):
    date = models.DateField(null=True)
    note = models.CharField(max_length=500)
    grade = models.IntegerField()


class Behavior(models.Model):
    type = models.BooleanField() #true=good, false=bad
    note = models.CharField(max_length=500)


class Homework(models.Model):
    text=models.CharField(max_length=500)
    subject=models.CharField(max_length=50)
    deadline = models.DateTimeField()




class Group(models.Model):
    name = models.CharField(max_length=100)
    schedule = models.ForeignKey(schedule, on_delete=models.CASCADE, null=True)
    homework = models.ManyToManyField(Homework)


class Student(models.Model):
    groups = models.ManyToManyField(Group)
    grades = models.ManyToManyField(Grade)
    behavior = models.ManyToManyField(Behavior)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)

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

