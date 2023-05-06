from django.db import models
# Import User model from the Django auth application
from django.contrib.auth.models import User
# Cloudinary import for image storage
from cloudinary.models import CloudinaryField
# Validators for user choices in profile and booking
from django.core.validators import MaxValueValidator, MinValueValidator


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
