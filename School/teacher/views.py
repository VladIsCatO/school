from django.shortcuts import render, redirect
from django_ratelimit.decorators import ratelimit
from  django.core.mail import send_mail, send_mass_mail

from base.models import Student, Grades, Group, Teacher

def teacher_home(request):
        if request.method == 'GET':
            maill = request.session.get('email', 'Не вказано')
            teacher_info = Teacher.objects.filter(email=maill).first()
            return render(request, 'teacher_home.html',{"teacher_info":teacher_info})
        else:
            return render(request, 'teacher_home.html', )#{'res':res}
