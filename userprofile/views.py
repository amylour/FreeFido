from django.shortcuts import render
from allauth.account.views import SignupView


class CustomSignupView(SignupView):
    template_name = 'account/signup.html'


# from django.shortcuts import render, redirect
# from .forms import UserProfileForm, DogForm
# from .models import UserProfile, Dog


# def profile_view(request):
#     """ A view to return the profile page """

#     # user_profile = UserProfile.objects.get(user=request.user)

#     return render(request, 'userprofile/profile.html')

#     # , {'user_profile': user_profile}


# def create_profile(request):
#     """ Create profile for the user upon SignUp """
#     if request.method == 'POST':
#         user_profile_form = UserProfileForm(request.POST)
#         dog_form = DogForm(request.POST)

#         if user_profile_form.is_valid() and dog_form.is_valid():
#             # save the user's entered data
#             user_profile = user_profile_form.save(commit=False)
#             user_profile.user = request.user
#             user_profile.save()
#             dog = dog_form.save(commit=False)
#             dog.user_profile = user_profile
#             dog.save()
#             return redirect('profile')
#     else:
#         user_profile_form = UserProfileForm()
#         dog_form = DogForm()

#     context = {
#         'user_profile_form': user_profile_form,
#         'dog_form': dog_form,
#     }
#     return render(request, 'create_profile.html', context)
