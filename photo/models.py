from django.db import models
# Import User model from the Django auth application
from django.contrib.auth.models import User
# Cloudinary import for image storage
from cloudinary.models import CloudinaryField


class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    caption = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username}'s photo {self.id}"
