from django.contrib import admin
from petstagram.web.models import Pet, PetPhoto


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    list_display = ('description', 'likes')
