from django.shortcuts import render, redirect
from django_ratelimit.decorators import ratelimit
from  django.core.mail import send_mail, send_mass_mail
from django.http import JsonResponse
import random
from .models import Student, Grades, Group, Teacher, Teacher_mails, Manager, Parents
from django.contrib.auth.models import User

def get_user_permissions(user):
    if Teacher.objects.filter(user=user).exists():
        return "teacher"
    elif Manager.objects.filter(user=user).exists():
        return "manager"
    elif Parents.objects.filter(user=user).exists():
        return "parent"
    elif Student.objects.filter(user=user).exists():
        return "student"
    else:
        return None


def home(request):
    
    return render(request, 'home.html')



# def create_acc(request):
#         if request.method == 'GET':
#             return render(request, 'create_acc.html',)
#         else:
#             email = request.POST.get("email")
#             res = "Ваш запит надіслано"
#             # recipt_us  = Userr.objects.get(name=user_del)
#             # send_mail('Замовлення', f"Вас розбанено в кімнаті таємного санти."f" Імя кімнати:{room.room_name}. Код кімнати:{room.code}", "maksumkarmazyn98@ukr.net", [recipt_us.mail],fail_silently=False)
#             return render(request, 'create_acc.html', {'res':res})
