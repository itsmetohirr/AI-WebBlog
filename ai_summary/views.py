import json
import re
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from pytube import YouTube


from .forms import CustomUserCreationForm
from .functions import get_transcript, summarize_transcript, get_video_title
from .models import AI_Summary


def home_view(request):
    return render(request, 'home.html')


@csrf_exempt
def generate_blog(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            youtube_link = data.get('link')
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid data sent'}, status=400)
        
        title = get_video_title(youtube_link)
        transcript = get_transcript(youtube_link)
        content = summarize_transcript(transcript)

        if not request.user.is_anonymous:
            new_summary = AI_Summary(
                user=request.user,
                youtube_title=title,
                youtube_link=youtube_link,
                content=content
            )
            new_summary.save()

        return JsonResponse({'content': content})

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


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


def blog_list(request):
    all_articles = AI_Summary.objects.get()


    context = {'articles': all_articles}

    return render(request, 'all-blogs.html', context)
