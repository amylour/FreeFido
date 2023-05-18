from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('findus/', views.findus_view, name='findus'),
]
