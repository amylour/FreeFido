from django.db import models
# Import User model from the Django auth application
from django.contrib.auth.models import User
# Cloudinary import for image storage
from cloudinary.models import CloudinaryField
# Validators for user choices in profile and booking
from django.core.validators import MaxValueValidator, MinValueValidator


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    profile_pic = CloudinaryField('profile_pic', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    # method to return a string representation of an object - Django Docs magic method
    def __str__(self):
        return self.user.username


class Dog(models.Model):
    # Breed choices for user in profile dropdown menu in tuple format for database value and site viewable value for the user
    BREED_CHOICES = [
        ('Australian Shepard', 'Australian Shepard'),
        ('Bassett Hound', 'Bassett Hound'),
        ('Beagle', 'Beagle'),
        ('Belgian Shepard', 'Belgian Shepard'),
        ('Bernese', 'Bernese'),
        ('Bichon Frise', 'Bichon Frise'),
        ('Boston Terrier', 'Boston Terrier'),
        ('Boxer', 'Boxer'),
        ('Bulldog', 'Bulldog'),
        ('Chihuahua', 'Chihuahua'),
        ('Collie', 'Collie'),
        ('Corgi', 'Corgi'),
        ('Dachshund', 'Dachshund'),
        ('Doberman', 'Doberman'),
        ('English Mastiff', 'English Mastiff'),
        ('Fox Hound', 'Foxhound'),
        ('Greyhound', 'Greyhound'),
        ('German Shepherd', 'German Shepherd'),
        ('Golden Retriever', 'Golden Retriever'),
        ('Great Dane', 'Great Dane'),
        ('Husky', 'Husky'),
        ('Labrador Retriever', 'Labrador Retriever'),
        ('Lurcher', 'Lurcher'),
        ('Poodle', 'Poodle'),
        ('Rottweiler', 'Rottweiler'),
        ('Saint Bernard', 'Saint Bernard'),
        ('Shih Tzu', 'Shih Tzu'),
        ('Spaniel', 'Spaniel'),
        ('Terrier', 'Terrier'),
        ('Weimaraner', 'Weimaraner'),
        ('Other', 'Other'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    dog_name = models.CharField(max_length=20)
    breed = models.CharField(max_length=30, choices=BREED_CHOICES)
    color = models.CharField(max_length=30)
    is_vaccinated = models.BooleanField(default=False)
    gender = models.CharField(max_length=6, choices=[
                              ('M', 'Male'), ('F', 'Female')])

    def __str__(self):
        return f"{self.user.username}'s dog {self.dog_name}"
