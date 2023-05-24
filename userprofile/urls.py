from django.urls import path
from .views import add_user, profile_view, edit_profile

urlpatterns = [
    path('account/signup/', add_user.as_view(), name='account_signup'),
    path('profile/', profile_view, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
]
