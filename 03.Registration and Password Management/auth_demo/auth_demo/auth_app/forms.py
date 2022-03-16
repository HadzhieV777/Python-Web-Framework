from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

from auth_demo.auth_app.models import Profile

UserModel = get_user_model()


class UserRegistrationForm(auth_forms.UserCreationForm):
    """
    The Open-Closed Principle (OCP) states that software entities (classes, modules, methods, etc.)
    should be open for extension, but closed for modification.
    In practice, this means creating software entities whose behavior can be changed
    without the need to edit and recompile the code itself.
    """

    first_name = forms.CharField(max_length=25)

    class Meta:
        model = UserModel
        fields = ('email',)

    # class Meta:
    #     model = UserModel
    #     fields = ('username', 'first_name')
    #
    def clean_first_name(self):
        return self.cleaned_data['first_name']

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            **self.cleaned_data,
            user=user,
        )
        if commit:
            profile.save()

        return user

    # class ProfileCreateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         exclude = ('user',)
