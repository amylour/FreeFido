from django.shortcuts import render


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def login_view(request):
    """ A view to return the login page """
    return render(request, 'home/login.html')
