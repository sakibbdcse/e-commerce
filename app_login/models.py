from django.db import models
# to create a custom user models and admin penel

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
# from django.utils.translation import ugettext_lazy

# Create your models here.

class myUserManager (BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('email reqired!')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # supper user creation

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('super user must have is_staff = Ture')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('super user must be is_superuser=True')
        
        return self._create_user(email, password, **extra_fields)