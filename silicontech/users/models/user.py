from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    """Define a model manager for User model with no usernational_id field."""

    use_in_migrations = True

    def _create_user(self, name, national_id, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not national_id:
            raise ValueError('The given national_id must be set')
        if not name:
            raise ValueError('The given name must be set')

        user = self.model(name=name, national_id=national_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, name, national_id, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(name, national_id, password, **extra_fields)

    def create_superuser(self, name, national_id, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(name, national_id, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    national_id = models.PositiveIntegerField('ID', unique=True)
    is_staff = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "national_id"
    REQUIRED_FIELDS = ["name"]

    def get_username(self):
        return str(self.national_id)
