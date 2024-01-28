from django import forms
from .models import Anime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ['code', 'name', 'type', 'image', 'status', 'comment']

class RegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']