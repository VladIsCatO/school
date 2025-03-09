from django.shortcuts import render, redirect
from django_ratelimit.decorators import ratelimit
from  django.core.mail import send_mail, send_mass_mail
from django.http import JsonResponse
import random
from base.models import Teacher_mails
# Create your views here.
def home(request):
    return render(request, 'home_manager.html')

def login(request): 
    return render(request, 'login.html')

def add_teacher(request):
    if request.method == 'GET':
        return render(request, 'add_teacher.html')
    email = request.POST.get("email")
    tm = Teacher_mails(email=email)
    tm.save()
    send_mail('Підтверджено як вчителя', f"Ваш email для входу:"f"{email}.", from_email="maksumkarmazyn98@ukr.net", recipient_list=[email],fail_silently=False)
    return redirect('/manager/home', {'res': 'Збережено'})