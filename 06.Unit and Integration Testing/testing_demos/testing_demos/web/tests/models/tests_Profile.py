from django.core.exceptions import ValidationError
from django.test import TestCase

from testing_demos.web.models import Profile


class ProfileTests(TestCase):
    VALID_PROFILE_DATA = {
        'first_name': 'Rado',
        'last_name': 'Hadzhiev',
        'age': 24,
    }

    def test_profile_create__when_first_name_contains_only_letters__expect_success(self):
        profile = Profile(**self.VALID_PROFILE_DATA)
        profile.save()
        self.assertIsNotNone(profile.pk)

    def test_profile_create__when_first_name_contains_a_digit__expect_to_fail(self):
        first_name = 'Rado22'
        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_PROFILE_DATA['last_name'],
            age=self.VALID_PROFILE_DATA['age'],
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()  # This is called in ModelForms implicitly but here we need to call it
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_create__when_first_name_contains_a_dollar_sign__expect_to_fail(self):
        first_name = 'Ra$do'
        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_PROFILE_DATA['last_name'],
            age=self.VALID_PROFILE_DATA['age'],
        )
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()  # This is called in ModelForms implicitly but here we need to call it
            profile.save()

    def test_profile_create__when_first_name_contains_a_space__expect_to_fail(self):
        first_name = 'Ra do'
        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_PROFILE_DATA['last_name'],
            age=self.VALID_PROFILE_DATA['age'],
        )
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()  # This is called in ModelForms implicitly but here we need to call it
            profile.save()

    def profile_full_name__when_valid__expect_correct_full_name(self):
        profile = Profile(**self.VALID_PROFILE_DATA)

        expected_full_name = f'{self.VALID_PROFILE_DATA["first_name"]} {self.VALID_PROFILE_DATA["last_name"]}'
        self.assertEqual(expected_full_name, profile.full_name)
