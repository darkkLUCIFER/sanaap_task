from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from apps.accounts.managers import UserManager
from apps.accounts.validators import phone_regex_validator


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=12, unique=True, validators=[phone_regex_validator],
                                    verbose_name="Phone Number")

    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'

    def __str__(self):
        return self.phone_number
