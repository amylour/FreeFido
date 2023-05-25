from django.db import models
# Import User model from the Django auth application
from django.contrib.auth.models import User
# Cloudinary import for image storage
from cloudinary.models import CloudinaryField
# Validators for user choices in profile and booking
# from django.core.validators import MaxValueValidator, MinValueValidator


class AccountProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = CloudinaryField('profile_pic', blank=True)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20, blank=True)

    # method to return a string representation of an object - Django Docs magic method
    def __str__(self):
        return self.user.first_name
