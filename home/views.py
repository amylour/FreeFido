from django.shortcuts import render


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def findus_view(request):
    """ A view to return the find us page """
    return render(request, 'home/findus.html')

