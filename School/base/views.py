from django.shortcuts import render, redirect
from django_ratelimit.decorators import ratelimit
from  django.core.mail import send_mail, send_mass_mail
from django.http import JsonResponse
import random
from .models import Student, Grades, Group, Teacher, Teacher_mails
from django.contrib.auth.models import User
@ratelimit(key='ip', rate='5/20sec', method='POST', block=True)
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html',)
    else:
        res = "неправельний пароль"
        ver_code = request.session.get('ver_code', None)
        ver_code1 = request.POST.get("ver_code1", "")
        if ver_code == ver_code1:
                email = request.POST.get("email")
                name = request.POST.get("username")
                password = request.POST.get("password")
                user = User(email=email, username=name, password=password)
                user.save()
                return redirect('/teacher/home', {'res':'Вхід успішний'})
    return render(request, 'login.html', {'res':res})

def home(request):
    return render(request, 'home.html')

def teacher_check(request):
    if request.method == 'GET':
        return JsonResponse({'res': 'Error: wrong method, try POST'})
    email = request.POST.get("email")
    print(email)
    print(request.POST)
    # request.session['email'] = email
    teacher_mails = Teacher_mails.objects.filter(email=email).first()
    print(teacher_mails)
    if not teacher_mails:
        return JsonResponse({'res': 'Wrong email'})
    else:
        code = ""
        string = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
        for i in range(11):
            code += random.choice(string)
        request.session['ver_code'] = code
        send_mail('Підтвердження на вхід', f"Ваш код для входу:"f"{code}.", from_email="maksumkarmazyn98@ukr.net", recipient_list=[email],fail_silently=False)
        return JsonResponse({'res': 'Ok'}) #, 'code':code

# def create_acc(request):
#         if request.method == 'GET':
#             return render(request, 'create_acc.html',)
#         else:
#             email = request.POST.get("email")
#             res = "Ваш запит надіслано"
#             # recipt_us  = Userr.objects.get(name=user_del)
#             # send_mail('Замовлення', f"Вас розбанено в кімнаті таємного санти."f" Імя кімнати:{room.room_name}. Код кімнати:{room.code}", "maksumkarmazyn98@ukr.net", [recipt_us.mail],fail_silently=False)
#             return render(request, 'create_acc.html', {'res':res})
