from django.shortcuts import render


def profile_view(request):
    """ A view to return the profile page """

    return render(request, 'userprofile/profile.html')
