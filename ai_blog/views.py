from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import CustomUserCreationForm


def home_view(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})



    return render(request, 'login.html')


def signup_view(request):
    print('in sign up')
    if request.method == 'POST':
        print('request is post')
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print('form is valid')
            form.save()
            print('form saved')
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
        else:
            print('form is not valid')
            print(form.errors)
    else:
        print('form is not valid')
        form = CustomUserCreationForm()
    
    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    logout(request)

    return redirect('/')
