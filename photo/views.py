from django.shortcuts import render


def gallery_view(request):
    """ A view to return the gallery page """

    # photos = Photos.objects.all()

    return render(request, 'photo/gallery.html')
