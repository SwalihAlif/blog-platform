from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    CHOICES = [
        "author" = 'A'
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.