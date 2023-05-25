from django.shortcuts import render, redirect
from allauth.account.views import SignupView
from .models import AccountProfile
from .forms import AccountProfileForm


class add_user(SignupView):
    template_name = 'account/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)

        AccountProfile.objects.create(user=self.user)

        return response


def profile_view(request):
    """ A view to return the profile page """
    account_profile = AccountProfile.objects.get(user=request.user)

    context = {
        'account_profile': account_profile,
    }

    return render(request, 'userprofile/profile.html')


def edit_profile(request):
    """ Edit profile for user """

    if request.method == 'POST':
        account_profile_form = AccountProfileForm(request.POST)
        if account_profile_form.is_valid():
            # save the user's entered data
            account_profile = account_profile_form.save(commit=False)
            account_profile.user = request.user
            account_profile.save()
            return redirect('profile')
    else:
        account_profile_form = AccountProfileForm()

    context = {
        'account_profile_form': account_profile_form,
    }
    return render(request, 'edit_profile.html', context)
