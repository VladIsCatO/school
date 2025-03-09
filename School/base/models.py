from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, User

class Grades(models.Model):
    grade = models.IntegerField(null=True)

class Course(models.Model):
    name = models.CharField(max_length=100)
    groups = models.ManyToManyField(Group)

class Student(models.Model):
    courses = models.ManyToManyField(Course)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, related_name='student_groups')
    grades = models.ForeignKey(Grades, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)

class Teacher(models.Model):  # Teachers
    group = models.ManyToManyField(Group, related_name='teacher_groups')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)

class Manager(models.Model):  # Manager creates teacher's account and group adds students to groups
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)

class Parents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)

class Group(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ManyToManyField(Teacher, related_name='group_teachers')
    course = models.ManyToManyField(Course)
    students = models.ManyToManyField(Student, related_name='group_students')

class Teacher_mails(models.Model):
    email = models.EmailField(max_length=100)