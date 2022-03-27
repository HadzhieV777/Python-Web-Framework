from django import forms
from datetime import date

from petstagram.common.helpers import BootstrapFormsMixin, DisabledFieldsFormMixin
from petstagram.common.validators import MaxDateValidator
from petstagram.web.models import Pet, PetPhoto


class AddPetForm(forms.ModelForm, BootstrapFormsMixin):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        # commit false does not persist in database
        # just returns the object to be created
        pet = super().save(commit=False)  # taking the pet instance

        pet.user = self.user
        if commit:
            pet.save()

        return pet

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'label': 'Pet Name',
                    'placeholder': 'Enter pet Name'
                }
            ),
        }
        labels = {
            'type': 'Type',
            'date_of_birth': 'Date of Birth',
        }


class EditPetForm(BootstrapFormsMixin, forms.ModelForm):
    MIN_DATE_OF_BIRTH = date(1920, 1, 1)
    MAX_DATE_OF_BIRTH = date.today()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def clean_date_of_birth(self):
        MaxDateValidator(date.today())(self.cleaned_data['date_of_birth'])
        return self.cleaned_data['date_of_birth']

    class Meta:
        model = Pet
        exclude = ('user',)


class DeletePetForm(BootstrapFormsMixin, DisabledFieldsFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Pet
        exclude = ('user',)


class AddPetPhotoForm(forms.ModelForm, BootstrapFormsMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = PetPhoto
        fields = ('photo', 'description', 'tagged_pets')
        widgets = {
            'description': forms.TextInput(
                attrs={
                    'label': 'Description',
                    'placeholder': 'Enter description'
                }
            ),
        }
        labels = {
            'photo': 'Pet Image',
            'tagged_pets': 'Tag Pets',
        }


class DeletePetPhotoForm(BootstrapFormsMixin, DisabledFieldsFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = PetPhoto
        exclude = ('user',)
