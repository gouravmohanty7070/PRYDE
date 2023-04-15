from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# @login_required
@csrf_exempt
def HomePage(request):
    # if request.user.is_authenticated:
    #     return render(request, 'auth_system/index.html', {})
    # else:
    #     return redirect("auth-page")
    return render(request, 'auth_system/index.html', {})

@csrf_exempt
def AuthenticationView(request):
    if request.user.is_authenticated:
        return redirect("home-page")
    else:
        return render(request, 'auth_system/register.html')

@csrf_exempt
def registerUser(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['cpass']
        errors = []
        if (password != confirm_password):
            errors.append('Password not matching')
        if (len(name) < 3):
            errors.append('Enter Username')
        if (User.objects.filter(username=name)):
            errors.append('Username exists')
        if (User.objects.filter(email=email)):
            errors.append('Email Exists')
        if(len(errors)):
            print(errors)
            context = {
                'errors': errors,
                'type': 'register'
            }
            return render(request, 'auth_system/register.html', context=context)
        User.objects.create_user(username=name, email=email, password=password)
        return render(request, 'auth_system/register.html')
    else:
        return redirect("auth-page")

@csrf_exempt
def loginUser(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST['name']
        password = request.POST['password']

        print(name, password)

        user = authenticate(request, username=name, password=password)

        if user is not None:
            print('hello')
            login(request, user)
            return redirect('home-page')
        else:
            return HttpResponse("Error, user doesn't exist")
    else:
        return redirect("auth-page")

@csrf_exempt
def logoutUser(request):
     logout(request)
     return redirect('loginUser') 