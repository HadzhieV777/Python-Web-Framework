from django.core import validators
from django.db import models


class Category(models.Model):
    NAME_MAX_LENGTH = 15

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )


class Product(models.Model):
    NAME_MAX_LEN = 25
    PRICE_MIN_VALUE = 0

    name = models.CharField(
        max_length=NAME_MAX_LEN,
    )
    price = models.FloatField(
        validators=(
            validators.MinValueValidator(PRICE_MIN_VALUE),
        )
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
