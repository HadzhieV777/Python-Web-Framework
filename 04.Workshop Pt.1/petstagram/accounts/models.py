from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models

from petstagram.accounts.managers import PetstagramUserManager

'''
1. Create model extending ...
2. Configure this model in settings.py
3. Create user manager
'''


class PetstagramUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LEN = 25

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        unique=True,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = PetstagramUserManager()


class Profile(models.Model):
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 30

    ONLY_LETTERS_VALIDATOR_ERROR = "Ensure this value contains only letters."

    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 30

    # choices
    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            RegexValidator(r'^[a-zA-Z]+$', ONLY_LETTERS_VALIDATOR_ERROR),
        ),
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            RegexValidator(r'^[a-zA-Z]+$', ONLY_LETTERS_VALIDATOR_ERROR),
        ),
    )
    image = models.URLField()
    date_of_birth = models.DateField(
        null=True,
        blank=True,

    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    email = models.EmailField(
        null=True,
        blank=True,
    )
    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        null=True,
        blank=True,
        default=DO_NOT_SHOW,
    )

    #  Remove field id from profile
    #  Add field user to profile
    user = models.OneToOneField(
        # we can use the PetstagramUser model instead of get_user_model()
        # because it is in the same file as Profile
        PetstagramUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
