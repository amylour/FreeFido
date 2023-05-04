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

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dog_name = models.CharField(max_length=20)
    breed = models.CharField(max_length=30, choices=BREED_CHOICES)
    color = models.CharField(max_length=30)
    is_vaccinated = models.BooleanField(default=False)
    gender = models.CharField(max_length=6, choices=[
                              ('M', 'Male'), ('F', 'Female')])

    def __str__(self):
        return f"{self.user.username}'s dog {self.dog_name}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    # Max three dogs per person
    booking_for = models.PositiveIntegerField(
        validators=[MaxValueValidator(3)])
    # confirmation of booking email sent
    mail_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s booking on {self.date}"


class Feedback(models.Model):
    booking = models.ForeignKey('Booking', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(max_length=250)
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username}'s Feedback for booking {self.booking.id}"

    # # Django save method to save an instance of the user's feedback to the database
    # def save(self, *args, **kwargs):
    #     super(Feedback, self).save(*args, **kwargs)
    #     if self.booking.user.email:
    #         # replace this with email details once created


class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    caption = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username}'s photo {self.id}"
