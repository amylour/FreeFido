from django.urls import path
from .views import add_user, profile_view, create_profile

urlpatterns = [
    path('account/signup/', add_user.as_view(), name='account_signup'),
    path('profile/', profile_view, name='profile'),
    path('create_profile/', create_profile, name='create_profile'),
]


#
# from . import views


# urlpatterns = [
#     path('profile/', views.profile_view, name='profile'),
#     path('create_profile/', views.create_profile, name='create_profile'),
# ]
