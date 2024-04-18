from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import  login, logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Exam,Exam4,Exam3,Exam2



# Create your views here.
def Lg_page(request):
    if request.method == 'POST':
        user = authenticate(request=request,data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username = username , password = password)

        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid username')            
            return redirect('/')  
             
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/log')
        else:
            login(request,user)
            return redirect('/')
        
    return render(request, 'app/login.html')

def logout_page(request):
    logout(request)
    return redirect('/log')

def reg_page(request):
    if request.method == 'POST':
        user = authenticate(request=request,data=request.POST)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = User.objects.filter(username = username)
        if user.exists():
            messages.error(request, 'Username alredy taken')
            return redirect('/reg')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )
        user.set_password(password)
        user.save()

        user = User.objects.all()

        messages.success(request, 'Account created Sucessfully')
        return redirect('/log')

    return render(request,'app/register.html')

def que_page(request):
    if request.method == 'POST':
        que = request.POST.get('que')
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        option4 = request.POST.get('option4')
        correctans = request.POST.get('correctans')

        new_data = Exam(Question=que,Option1=option1,Option2=option2,Option3=option3,Option4=option4,Corrans=correctans)
        new_data.save()

        # new_data = Exam.objects.all()

        messages.success(request, 'Data Store Sucessfully')
        return redirect('/addque')

    return render(request,'app/addque.html')

def que2_page(request):
    if request.method == 'POST':
        que = request.POST.get('que')
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        option4 = request.POST.get('option4')
        correctans = request.POST.get('correctans')

        new_data = Exam2(Question=que,Option1=option1,Option2=option2,Option3=option3,Option4=option4,Corrans=correctans)
        new_data.save()

        # new_data = Exam.objects.all()

        messages.success(request, 'Data Store Sucessfully')
        return redirect('/addque2')

    return render(request,'app/addque2.html')

def que3_page(request):
    if request.method == 'POST':
        que = request.POST.get('que')
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        option4 = request.POST.get('option4')
        correctans = request.POST.get('correctans')

        new_data = Exam3(Question=que,Option1=option1,Option2=option2,Option3=option3,Option4=option4,Corrans=correctans)
        new_data.save()

        # new_data = Exam.objects.all()

        messages.success(request, 'Data Store Sucessfully')
        return redirect('/addque3')

    return render(request,'app/addque3.html')

def que4_page(request):
    if request.method == 'POST':
        que = request.POST.get('que')
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        option4 = request.POST.get('option4')
        correctans = request.POST.get('correctans')

        new_data = Exam4(Question=que,Option1=option1,Option2=option2,Option3=option3,Option4=option4,Corrans=correctans)
        new_data.save()

        # new_data = Exam.objects.all()

        messages.success(request, 'Data Store Sucessfully')
        return redirect('/addque4')

    return render(request,'app/addque4.html')

@login_required(login_url='/log')
def home(request):
    if request.method == 'GET':
        print("Called.....")
        exam = Exam.objects.all()
        return render(request, 'app/home.html', {'exam':exam})
    
def q2_list(request):
    print("Called.....")
    exam2 = Exam2.objects.all()
    return render(request, 'app/questions2.html',{'exam2':exam2})

def q3_list(request):
    exam3 = Exam3.objects.all()
    return render(request, 'app/questions3.html',{'exam3':exam3})

def q4_list(request):
    exam4 = Exam4.objects.all()
    return render(request, 'app/questions4.html',{'exam4':exam4})
