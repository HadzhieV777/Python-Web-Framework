from django.contrib.auth import models as auth_models
from django.contrib.auth.models import User
from django.db import models

from auth_demo.auth_app.managers import AppUsersManager


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    # django will use the USERNAME_FIELD to validate the user instead of username
    USERNAME_FIELD = 'email'

    objects = AppUsersManager()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
    )

    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )


'''
1. Create a model extending AbstractBaseUser and PermissionsMixin
2. Tell Django for your user model 
 - in settings.py by defining AUTH_USER_MODEL = 'auth_app.AppUser'
3. Create user manager
'''
# class UserWithFullNameProxy(UserModel):
#     @property
#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'


# # User with profile
# class Profile(models.Model):
#     # fields
#     # profile image
#     # date_of_birth
#     # pets
#
#     user = models.OneToOneField(
#         UserModel,
#         on_delete=models.CASCADE
#     )


# # Only user model extending the base
# class CustomUser:
#     # fields
#     # profile image
#     # date_of_birth
#     # pets
#
#     user = models.OneToOneField(
#         UserModel,
#         on_delete=models.CASCADE
#     )


# # Almost completely custom user model
# class AppUser:
#     pass
#     # email
#     # password
#     # is_staff
#     # is_superuser


# class Profile:
#     # first name
#     # last_name
#     # profile img
#     user = models.OneToOneField(
#         UserModel,
#         on_delete=models.CASCADE
#     )
