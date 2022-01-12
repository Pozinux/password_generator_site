from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, "password_generator_app_templates/home.html")

def password_function(request):

    characters = list("abcdefghijklmnopqrstuvwxyz")

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('lenght', 12))

    the_password = ''
    for x in range(length):
            the_password += random.choice(characters)

    return render(request, "password_generator_app_templates/password.html", {'password_dict_key': the_password})

def about_function(request):
   return render(request, "password_generator_app_templates/about.html") 
