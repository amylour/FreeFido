from django.shortcuts import render
from .models import UserProfile


def profile(request):
    """ A view to return the user profile page """

    # Get UserProfile for current user
    userprofile = UserProfile.objects.get(user=request.user)
    # Add to the template html file
    context = {'userprofile': userprofile}
    # Show user data on profile page
    return render(request, 'userprofile/profile.html', context)
