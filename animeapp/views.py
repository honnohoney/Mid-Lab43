from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login

from .forms import AnimeForm, RegistrationForm
from .models import Anime

class CustomLoginView(LoginView):
    template_name = 'login.html'

def home(request):
    return render(request, "base.html")

def anime_list(request):
    anime_list = Anime.objects.all()
    return render(request, 'anime/list.html', {'anime_list': anime_list})

def add_anime(request):
    if request.method == 'POST':
        form = AnimeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('anime-list')  
    else:
        form = AnimeForm()
    return render(request, 'anime/add.html', {'form': form})


from django.db.models import Q

def search_view(request):
    query = request.GET.get('q') or request.POST.get('q')

    if query:
        anime_list = Anime.objects.filter(
            Q(name__icontains=query) |
            Q(status__icontains=query) |
            Q(type__icontains=query) 
        )
    else:
        anime_list = Anime.objects.all()

    return render(request, 'anime/list.html', {'anime_list': anime_list})


def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home')  
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def login_page(request):
    return render(request, "login.html")