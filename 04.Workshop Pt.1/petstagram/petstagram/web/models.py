from django.contrib.auth import get_user_model

from django.db import models

import datetime

from petstagram.common.validators import MaxFileSizeInMbValidator

# UserModel gives the abstract user class which we have defined on app lvl(app settings)
UserModel = get_user_model()


class Pet(models.Model):
    NAME_MAX_LEN = 30

    CAT = "Cat"
    DOG = "Dog"
    BUNNY = "Bunny"
    PARROT = "Parrot"
    FISH = "Fish"
    OTHER = "Other"

    TYPES = [(x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]
    name = models.CharField(
        max_length=NAME_MAX_LEN,
    )
    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        # MinDateValidator(),
    )
    user = models.ForeignKey(  # select the user profile
        UserModel,  # it's better to refer to the UserModel, not to Profile
        on_delete=models.CASCADE
        # Alter unique_together for pet (0 constraint(s))
        # Add field user to pet
        # Alter unique_together for pet (1 constraint(s))
        # Remove field user_profile from pet
    )

    def __str__(self):
        return f'{self.name} {self.type}'

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    class Meta:  # All pets' names should be unique for that user.
        unique_together = ('user', 'name')


class PetPhoto(models.Model):
    IMAGE_MAX_SIZE_IN_MB = 5
    IMAGE_UPLOAD_TO_DIR = 'pet_photos/'

    photo = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR,
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        ),
    )
    tagged_pets = models.ManyToManyField(
        Pet,
        # validate at least 1 pet
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    publication_date = models.DateTimeField(
        auto_now_add=True,
    )
    likes = models.IntegerField(
        default=0,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('publication_date',)


'''
# Pet has a profile relation
SELECT *
FROM Pets p
JOIN Profiles pr
ON p.profile_id = pr.id
JOIN Users u
ON pr.user_id == u.id
WHERE u.id == request.user.id

# Pet has a user relation
SELECT *
FROM Pets p
JOIN Users u
ON p.user_id == u.id
WHERE u.id == request.user.id
'''
