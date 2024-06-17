from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.CharField(max_length=500)
    image = models.ImageField(default="default.jpeg", upload_to="profile_images")

    def __str__(self) -> str:
        return self.user.username
