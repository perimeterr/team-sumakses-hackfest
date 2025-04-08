from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('provider', 'Resource Provider'),
        ('upcycler', 'Upcycler'),
    ]
    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default='provider',
    )
    name = models.CharField(max_length=255, verbose_name="User Name") # Added Name
    description = models.TextField(blank=True, verbose_name="User Description") # Added Description
    location = models.CharField(max_length=255, verbose_name="User Location") # Added Location

    def __str__(self):
        return self.username