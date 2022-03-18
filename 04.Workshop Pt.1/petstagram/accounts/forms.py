from django.contrib.auth import forms as auth_forms, get_user_model

from petstagram.accounts.models import Profile
from petstagram.common.helpers import BootstrapFormsMixin
from django import forms

from petstagram.web.models import PetPhoto


class CreateProfileForm(auth_forms.UserCreationForm, BootstrapFormsMixin):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LEN
    )
    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LEN
    )
    image = forms.URLField()
    date_of_birth = forms.DateField()
    description = forms.CharField(
        widget=forms.Textarea,
    )
    email = forms.EmailField()
    gender = forms.ChoiceField(choices=Profile.GENDERS)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            description=self.cleaned_data['description'],
            email=self.cleaned_data['email'],
            gender=self.cleaned_data['gender'],
            user=user
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'description', 'image')
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'label': 'Username',
                    'placeholder': 'Enter Username'
                }
            ),
            'password1': forms.TextInput(
                attrs={
                    'label': 'Password',
                    'placeholder': 'Enter Password'
                }
            ),
            'password2': forms.TextInput(
                attrs={
                    'label': 'Confirm Password',
                    'placeholder': 'Confirm Password'
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'label': 'First Name',
                    'placeholder': 'Enter First Name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'label': 'Last Name',
                    'placeholder': 'Enter Last Name'
                }
            ),
            'image': forms.TextInput(
                attrs={
                    'label': 'Link to Profile Picture',
                    'placeholder': 'Enter URL'
                }
            ),
        }


class EditProfileForm(BootstrapFormsMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.initial['gender'] = Profile.DO_NOT_SHOW

    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter email',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter description',
                    'rows': 3,
                },
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'min': '1920-01-01',
                }
            )
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        # Not good
        # should be done with signals
        # because this breaks the abstraction of the auth app
        pets = list(self.instance.pet_set.all())
        PetPhoto.objects.filter(tagged_pets__in=pets).delete()
        self.instance.delete()

        return self.instance

    class Meta:
        model = Profile
        fields = ()
