from django.shortcuts import render, redirect
from allauth.account.views import SignupView
from .models import UserProfile, Dog
from .forms import UserProfileForm, DogForm


class add_user(SignupView):
    template_name = 'account/signup.html'


def profile_view(request):
    """ A view to return the profile page """
    return render(request, 'userprofile/profile.html')


def edit_profile(request):
    """ Edit profile for the user """

    user_profile_form = UserProfileForm(request.POST)
    dog_form = DogForm(request.POST)

    if user_profile_form.is_valid() and dog_form.is_valid():
        # save the user's entered data
        user_profile = user_profile_form.save(commit=False)
        user_profile.user = request.user
        user_profile.save()
        dog = dog_form.save(commit=False)
        dog.user_profile = user_profile
        dog.save()
        return redirect('profile')
    else:
        user_profile_form = UserProfileForm()
        dog_form = DogForm()

    context = {
        'user_profile_form': user_profile_form,
        'dog_form': dog_form,
    }
    return render(request, 'edit_profile.html', context)
