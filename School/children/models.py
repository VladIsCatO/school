from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, User
from base.models import Group, Teacher, Teacher_mails, Manager


class Lesson(models.Model):
    Headline = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    date =models.DateTimeField()



class Homework(models.Model):
    text=models.CharField(max_length=500)
    deadline = models.DateTimeField()


class Grade(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    note = models.CharField(max_length=500)
    grade = models.IntegerField()


class Behavior(models.Model):
    type = models.BooleanField() #true=good, false=bad
    note = models.CharField(max_length=500)



class Student(models.Model):
    groups = models.ManyToManyField(Group)
    grades = models.ManyToManyField(Grade)
    behavior = models.ManyToManyField(Behavior)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)


class Group_Lessons(models.Model):
    group_name = models.CharField(Group,max_length=100)
    lessons = models.ManyToManyField(Lesson)
    students = models.ManyToManyField(Student)


    


class Student_mails(models.Model):
    email = models.EmailField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    code = models.CharField(max_length=50, null=True)