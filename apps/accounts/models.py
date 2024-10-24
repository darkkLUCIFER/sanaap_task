from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from apps.accounts.managers import UserManager
from apps.accounts.validators import phone_regex_validator


class User(AbstractBaseUser, PermissionsMixin):
    REGULAR = 'regular'
    ADMIN = 'admin'

    USER_TYPE_CHOICES = [
        (REGULAR, 'Regular'),
        (ADMIN, 'Admin'),
    ]

    phone_number = models.CharField(max_length=12, unique=True, validators=[phone_regex_validator],
                                    verbose_name="Phone Number")
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default=REGULAR, verbose_name="User Type")
    is_superuser = models.BooleanField(default=False, verbose_name="Superuser")
    is_staff = models.BooleanField(default=False, verbose_name="Staff")
    is_active = models.BooleanField(default=True, verbose_name="Active")

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'

    def __str__(self):
        return self.phone_number
