from django.shortcuts import render, redirect
from django_ratelimit.decorators import ratelimit
from  django.core.mail import send_mail, send_mass_mail
from django.contrib.auth import login
from base.models import Group, Teacher, Teacher_mails, Manager, Student
from .models import Student_mails
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.forms import AuthenticationForm
import random


def home(request):
    return render(request, 'dashboard.html')

def activate(request):
    if request.method == "GET":
        return render(request, "activate.html")
    code = request.GET.get('code')
    sm = Student_mails.objects.filter(code=code).first()
    if not sm:
        return render(request, "activate.html", {'res':'Wrong code'})
    user = User(username=request.POST.get("username"), password=request.POST.get("password"), email=sm.email)
    user.save()
    login(request, user)
    student = Student(user=request.user, email=sm.email)
    student.save()
    student.groups.add(sm.group)
    student.save()
    for i in Student_mails.objects.filter(email=sm.email):
        i.delete()
    return redirect("/students/")

def homework_page(request):
    if request.method == "GET":
        res = ''
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        print(Group.objects.filter(name=request.GET.get('name')).first())
        group =  Group.objects.filter(name=request.GET.get('name')).first()
        try:
            homeworks = group.homework.all()
        except:
            homeworks = None
        if group is not None:
            schedule_ = {}
            dbschedule = group.schedule.day.all()
            for i in dbschedule:
                schedule_[i.day]=i.lesson.all()
            schedule_ = schedule_.items()
        else:
            schedule_ = None
        if request.method == 'GET':
            return render(request, "group.html", {'group':group, 'students':Student.objects.filter(groups__in=[group]).all(), 'res':res, 'schedule':schedule_, 'days':days, 'homework':homeworks})
        