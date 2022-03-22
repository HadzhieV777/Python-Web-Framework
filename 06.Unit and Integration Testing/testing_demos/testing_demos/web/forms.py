from django import forms
from django.forms import modelform_factory

from testing_demos.web.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


# we can also use a modelform_factory for testing
# ProfileForm2 = modelform_factory(Profile, fields='__all__')