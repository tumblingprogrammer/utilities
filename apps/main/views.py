from django.shortcuts import render
import random


def home(request):
    return render(request, 'main/home.html', context=None)


def profile(request):
    return render(request, 'main/profile.html', context=None)


def slugifier(request):
    return render(request, 'main/slugifier.html', context=None)


def django_secret_key_generator(request):
    context = {}
    django_secret_key = ''
    for i in range(50):
        django_secret_key += random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')
        context['django_secret_key'] = django_secret_key
    return render(request, 'main/django-secret-key-generator.html', context=context)




