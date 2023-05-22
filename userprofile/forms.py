from django import forms
from .models import UserProfile, Dog


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'phone', 'profile_pic']


class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['dog_name', 'breed', 'color', 'is_vaccinated', 'gender']
