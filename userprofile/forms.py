from django import forms
from .models import AccountProfile


class AccountProfileForm(forms.ModelForm):
    class Meta:
        model = AccountProfile
        fields = ['profile_pic', 'first_name',
                  'last_name', 'phone']
