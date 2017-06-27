from django.shortcuts import render
import random


def home(request):
    context={}
    context['meta_content'] = "Collection of utilities helpful for web developers who use django, python, javascript, css and other web technologies."
    return render(request, 'main/home.html', context=context)


def profile(request):
    return render(request, 'main/profile.html', context=None)


def slugifier(request):
    context={}
    context['meta_content'] = "App to slugify text, as well as help with the construction of image markdown links."
    return render(request, 'main/slugifier.html', context=context)


def django_secret_key_generator(request):
    context = {}
    context['meta_content'] = "App to generate django secret keys."
    django_secret_key = ''
    for i in range(50):
        django_secret_key += random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')
        context['django_secret_key'] = django_secret_key
    return render(request, 'main/django-secret-key-generator.html', context=context)


def about_tumbling_utilities(request):
    return render(request, 'main/about-tumbling-utilities.html', context=None)




