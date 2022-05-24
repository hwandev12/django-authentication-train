from django.contrib.auth.models import AbstractUser
from phonenumber_field.formfields import PhoneNumberField
from django.db import models


# create custom user model
class CustomUserModel(AbstractUser):
    parent_name = models.CharField(max_length=100)
    phone = models.IntegerField(default=998)
