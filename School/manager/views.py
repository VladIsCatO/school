from django.shortcuts import render, redirect
from django_ratelimit.decorators import ratelimit
from  django.core.mail import send_mail, send_mass_mail
from django.http import JsonResponse
import random
from django.db import IntegrityError
from base.models import Teacher_mails,Group,Course,Teacher
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home_manager.html')

def login(request): 
    return render(request, 'login.html')

def add_teacher(request):
    res = None
    if request.method == 'GET':
        return render(request, 'add_teacher.html')
    email = request.POST.get("email")
    tc = Teacher_mails.objects.filter(email = email)
    if not tc:
        tm = Teacher_mails(email=email)
        tm.save()
    else:
        res = "Вчитель з цим емейлом вже завчасно доданий"
        return render(request, 'add_teacher.html',res = res)
    send_mail('Підтверджено як вчителя', f"Ваш email для входу:"f"{email}.", from_email="maksumkarmazyn98@ukr.net", recipient_list=[email],fail_silently=False)
    return redirect('/manage', {'res': 'Збережено'})

def add_group(request):
    if request.method == 'GET':
        teacher = Teacher.objects.all()
        return render(request, 'create_group.html', {'teacher':teacher})
    group_name = request.POST.get("group_name")
    course = request.POST.get("course")
    teacher_email = request.POST.get("teacher_mail")
    print(teacher_email, 1000000000000000000000000000000000000000000000000000000000000000000000000022)
    teacher_group = Group.objects.filter(name=group_name).filter()
    if not teacher_group:
        try:
            course_db, _ = Course.objects.get_or_create(name=course)
            ts = Group(name=group_name, course=course_db)
            ts.save()
            # Перевірка наявності групи перед створенням
            if not Group.objects.filter(name=group_name, course=course_db).exists():
                teacher = Teacher.objects.filter(email=teacher_email).first()
                if teacher:
                    teacher.groups.add(ts)
                    teacher.save()
                    print(f"Група {group_name} успішно додана вчителю {teacher.email}")
                else:
                    print(f"Вчитель з email {teacher_email} не знайдений.")
            else:
                print(f"Група {group_name} вже існує для курсу {course_db.name}.")
        except IntegrityError as e:
            print(f"Помилка бази даних: {e}")
        except Exception as e:
            print(f"Виникла помилка: {e}")
        return redirect('/manage', {'res': 'Групу додано'})
    else:
        print(444444444444444444444444444444444444444)
    return render(request, 'create_group.html', {'res':'Неправильне імя групи, вже існує група з цим імям'})


def associate_teacher(request):
    if request.method == 'GET':
        teachers = Teacher.objects.all()
        groups = Group.objects.all()
        return render(request, "associate_teacher.html", {'teachers': teachers, 'groups': groups})

    if request.method == 'POST':
        print(request.POST)
        group_name = request.POST.get("group_name")
        teacher_mail = request.POST.get("teacher_mail")

        try:
            group = Group.objects.filter(name=group_name).first()
            teacher = Teacher.objects.filter(email=teacher_mail).get()
            print(group)
            print(teacher)
            try:
                # Знаходимо попереднього викладача для цієї групи
                # last_teacher = Teacher.objects.filter(groups__in=group).first()
                last_teacher = Teacher.objects.filter(groups__in=[group]).first()
                print(last_teacher, 2123123123)
                
                if not group:
                    messages.error(request, f'Група з іменем "{group_name}" не знайдена.')
                    return redirect("/manage")
        
                if not teacher:
                    messages.error(request, f'Викладач з email "{teacher_mail}" не знайдений.')
                    return redirect("/manage")
                
                if last_teacher:
                    last_teacher.groups.remove(group)
                    last_teacher.save()
            except:
                pass

            teacher.groups.add(group)
            teacher.save()
            print('123')
            return redirect("/manage", {'res': f'Succesfully changed teacher of group {group.name}'})

        except Group.DoesNotExist:
            return redirect("/manage", {'res': f'Group {group_name} does not exist'})
        except Teacher.DoesNotExist:
            return redirect("/manage", {'res': f'Teacher with email {teacher_mail} does not exist'})
        except Exception as e:
            print(e)
            return redirect("/manage", {'res': f'An error occurred: {e}'})