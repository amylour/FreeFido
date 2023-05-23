from django.urls import path
from .views import CustomSignupView

urlpatterns = [
    path('account/signup/', CustomSignupView.as_view(), name='account_signup'),
]


# 
# from . import views


# urlpatterns = [
#     path('profile/', views.profile_view, name='profile'),
#     path('create_profile/', views.create_profile, name='create_profile'),
# ]
