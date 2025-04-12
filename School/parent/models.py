from django.db import models
from base.models import Student
from django.contrib.auth.models import User

# Create your models here.
class Parents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
