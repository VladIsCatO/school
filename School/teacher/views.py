from django.shortcuts import render, redirect
from django_ratelimit.decorators import ratelimit
from  django.core.mail import send_mail, send_mass_mail
from django.contrib.auth import login
from base.models import Student, Group, Teacher, Teacher_mails, Manager, Day, Schedule_lesson, schedule
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.forms import AuthenticationForm
from children.models import  Student_mails
import random
from base.views import get_user_permissions
import datetime

@ratelimit(key='ip', rate='5/20sec', method='POST', block=True)
def register_(request):
    if request.method == 'GET':
        # clean_db()
        # Teacher_mails(email='vladyslav.bankovskyi@gmail.com').save()
        return render(request, 'register.html', {})
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
                tm = Teacher_mails.objects.filter(email=email).first()
                tm.delete()
                request.session["mail"] = email
                return redirect('/teacher/', {'res':'Вхід успішний', 'permission':get_user_permissions(request.user)})
    return render(request, 'register.html', {'res':res})

def teacher_check(request):
    if request.method == 'GET':
        return JsonResponse({'res': 'Error: wrong method, try POST',})
    email = request.POST.get("email")
    request.session["mail"] = email
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

def gen_code():
    return "".join(random.choices("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890", k=11))

def send_verification_email(request, email):
    code = gen_code()
    request.session['ver_code'] = code

    html_message = render_to_string('verification_email.html', {'code': code}) #create verification_email.html
    request.session["mail"] = email
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
            if request.user.is_authenticated:
                print('asd')
                maill = request.session.get('mail', 'Не вказано')
                print(maill)
                teacher_info = Teacher.objects.filter(email=maill).first()
                for i in teacher_info.groups.all():
                    print(i, 10000000022222222222222222222)
                print(request.user)
                print(get_user_permissions(request.user))
                return render(request, 'teacher_home.html',{"teacher_info":teacher_info.groups.all(), 'permission':get_user_permissions(request.user)})
            return redirect('login')
        return redirect('teacher')


def clean_db():
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    groups = Group.objects.all()
    grades = Grades.objects.all()
    managers = Manager.objects.all()
    parents = Parents.objects.all()
    users = User.objects.all()
    mails = Teacher_mails.objects.all()
    db = [students, teachers, groups, grades, managers, parents, users, mails]
    for i in db:
        for j in i:
            j.delete()

@ratelimit(key='ip', rate='5/20sec', method='POST', block=True)
def login_(request):
    if request.method == 'GET':
        return render(request, 'login.html', {})
    else:
        email = request.POST.get("email")
        request.session["mail"] = email
        print(request.POST)
        password = request.POST.get("password")
        user = User.objects.filter(email=email).first()
        print(user.check_password(password))
        print(2111111111111111111111111111111111111111111111111111111111111)
        if user and user.password == password:
            print('logged in')
            login(request, user)
            return redirect('/teacher/', {'res':'Вхід успішний', 'permission':get_user_permissions(request.user), 'email':email})
        else:
            return render(request, 'login.html', {'res':'Неправильний логін або пароль'})
    
import pandas as pd

def structure_schedule_pandas(group):
    """
    Structures the schedule data from a Django Group object into a Pandas DataFrame.

    Args:
        group: An instance of the Django Group model.

    Returns:
        pandas.DataFrame or None: A DataFrame representing the schedule,
                                  or None if the group has no schedule.
    """
    if group.schedule:
        data = []
        dbschedule = group.schedule.day.all()
        for day_obj in dbschedule:
            day_name = day_obj.day
            lessons = day_obj.lesson.all()
            for lesson in lessons:
                data.append({
                    'day': day_name,
                    'subject': lesson.subject,
                    'lesson_number': lesson.lesson_number
                })
        if data:
            schedule_df = pd.DataFrame(data)
            return schedule_df
        else:
            return pd.DataFrame(columns=['day', 'subject', 'lesson_number']) # Return empty DataFrame if no lessons
    else:
        return None
def group(request):
    res = ''
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    print(Group.objects.filter(name=request.GET.get('name')).first())
    group =  Group.objects.filter(name=request.GET.get('name')).first()
    if group is not None:
        schedule_ = {}
        dbschedule = group.schedule.day.all()
        for i in dbschedule:
            schedule_[i.day]=i.lesson.all()
        # print(structure_schedule_pandas(group))
        schedule_ = schedule_.items()
    else:
        schedule_ = None
    if request.method == 'GET':
        return render(request, "group.html", {'group':group, 'students':Student.objects.filter(groups__in=[group]).all(), 'res':res, 'schedule':schedule_, 'days':days})
    

    if request.POST.get('form') == 'edit_schedule':
        day_ = request.POST.get('day')
        lesson_number = request.POST.get('lesson_number')
        print('test: ', day_, ';;;', lesson_number)
        day = group.schedule.day.filter(day=day_).first()
        lesson = day.lesson.filter(lesson_number=lesson_number).first()
        lesson.subject = request.POST.get('subject', 'немає')
        lesson.save()
        return render(request, "group.html", {'group':group, 'students':Student.objects.filter(groups__in=[group]).all(), 'res':res, 'schedule':schedule_, 'days':days})
    
    if request.POST.get('email') is not None:
        email = request.POST.get('email')
        code=gen_code()
        group = Group.objects.filter(name=request.POST.get('group')).first()
        print(group)
        student = Student_mails(email=email, group=group, code=code)
        student.save()
        link=f'https://emu-striking-bee.ngrok-free.app/students/activate?code={code}'
        html_message = render_to_string('verification_email.html', {'code': link}) #create verification_email.html
        send_mail(
            'Email Verification Link',
            f"Your verification link: {link}",
            from_email="maksumkarmazyn98@ukr.net",
            recipient_list=[email],
            fail_silently=False,
            html_message=html_message, 
        )
        res = f'successfully sent account activation email to "{email}"'
    else:
        pass
    students = Student.objects.filter(groups__in=[group]).all()
    return render(request, "group.html", {'group':group, 'students':students, 'res':res})





def schedule_create(request):

    if request.method == 'GET':
        maill = request.session.get('mail', 'Не вказано')
        print(maill)
        teacher_info = Teacher.objects.filter(email=maill).first()
        for info in teacher_info.groups.all():
            print(info.name)
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        range_ = range(1, 9)
        return render(request, "create_schedule.html", {"teacher_info":teacher_info.groups.all(), "days" : days, "range":range_,'group':request.GET.get('group'), 'permission':get_user_permissions(request.user)})

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    dbschedule = schedule()
    dbschedule.save()  # Зберігаємо порожній розклад, щоб отримати ID

    group = Group.objects.filter(name=request.POST.get('group_name')).first()
    print(group)
    group.schedule = dbschedule
    group.save()

    for day_ in days:
        day_obj = Day(day=day_)
        day_obj.save()
        for i in range(1, 9):  # Змінено на range(1, 9), щоб відповідати нумерації уроків (1-8)
            lesson_subject = request.POST.get(f'schedule[{day_}][{i}]', "немає")
            if lesson_subject == "":
                lesson_subject = "немає"
            print(day_, i, lesson_subject)
            lesson = Schedule_lesson(subject=lesson_subject, lesson_number=i)
            lesson.save()
            day_obj.lesson.add(lesson)
        dbschedule.day.add(day_obj)

    dbschedule.save() # Зберігаємо розклад з усіма днями та уроками

    return redirect('/teacher/', {'res':'Розклад успішно створено', 'permission':get_user_permissions(request.user)})

def group_test(request):
    print(12222222222222222222222222222222222222222222222222222222222222222222222222222222222223333333333333333333333333333333333333333111111111111111111)
    homework_inp = request.POST.get('homework_inp')
    if homework_inp:
        print(homework_inp, 00000000000000000000000000000000000000)
        return JsonResponse({"homework_inp" : homework_inp})
    print(12333333333333333333333333333322213)
    return render(request, "group.html", {})

