from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import User, AbstractUser


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    phone_number = models.CharField(max_length=30, blank=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone_number']

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
        super(CustomUser, self).save(*args, **kwargs)

    def has_perm(self, perm, obj=None):
        return False

    def has_module_perms(self, app_label):
        return False
