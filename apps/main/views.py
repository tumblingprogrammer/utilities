from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html', context=None)


def profile(request):
    return render(request, 'main/profile.html', context=None)




