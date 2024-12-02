from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
# You define database models here (e.g., CustomUser).

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    # Add additional fields if needed
    phone_number = models.CharField(max_length=15, blank=True)
    shoe_size = models.PositiveIntegerField(null =True,
        validators=[
            MinValueValidator(30, message='Shoe size cannot be smaller than 30'),
            MaxValueValidator(50, message='Shoe size cannot be larger than 50')
        ]
    )