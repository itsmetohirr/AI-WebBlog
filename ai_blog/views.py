from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm


def home_view(request):
    return render(request, 'home.html')


def login_view(request):
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
    return render(request, 'logout.html')
