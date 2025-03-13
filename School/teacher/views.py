from django.shortcuts import render, redirect
from django_ratelimit.decorators import ratelimit
from  django.core.mail import send_mail, send_mass_mail
from django.contrib.auth import login
from base.models import Student, Grades, Group, Teacher, Teacher_mails, Manager, Parents
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.template.loader import render_to_string
import random


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

@ratelimit(key='ip', rate='5/20sec', method='POST', block=True)
def login_(request):
    if request.method == 'GET':
        clean_db()
        return render(request, 'login.html',)
    else:
        res = "неправельний пароль"
        ver_code = request.session.get('ver_code', None)
        ver_code1 = request.POST.get("ver_code1", "")
        if ver_code == ver_code1:
                email = request.POST.get("email")
                name = request.POST.get("username")
                password = request.POST.get("password")
                print(request.POST)
                user = User(email=email, username=name, password=password)
                user.save()
                login(request,user)
                teacher = Teacher(user=user, email=email)
                teacher.save()
                return redirect('/teacher/home', {'res':'Вхід успішний', 'permission':get_user_permissions(request.user)})
    return render(request, 'login.html', {'res':res})

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
        send_verification_email(request, email)
        return JsonResponse({'res': 'Ok'}) #, 'code':code

def send_verification_email(request, email):
    code = "".join(random.choices("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890", k=11))
    request.session['ver_code'] = code

    html_message = render_to_string('verification_email.html', {'code': code}) #create verification_email.html

    send_mail(
        'Email Verification Code',
        f"Your verification code: {code}",
        from_email="maksumkarmazyn98@ukr.net",
        recipient_list=[email],
        fail_silently=False,
        html_message=html_message, 
    )
    return JsonResponse({'res': 'Ok'})

def teacher_home(request):
        if request.method == 'GET':
            maill = request.session.get('email', 'Не вказано')
            teacher_info = Teacher.objects.filter(email=maill).first()
            print(request.user)
            print(get_user_permissions(request.user))
            return render(request, 'teacher_home.html',{"teacher_info":teacher_info, 'permission':get_user_permissions(request.user)})
        else:
            return render(request, 'teacher_home.html', )#{'res':res}


def clean_db():
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    groups = Group.objects.all()
    grades = Grades.objects.all()
    managers = Manager.objects.all()
    parents = Parents.objects.all()
    users = User.objects.all()
    db = [students, teachers, groups, grades, managers, parents, users]
    for i in db:
        for j in i:
            j.delete()