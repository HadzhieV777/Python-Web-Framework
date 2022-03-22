from django.test import TestCase
from django.urls import reverse

from testing_demos.web.models import Profile


class ProfileCreateViewTest(TestCase):
    VALID_PROFILE_DATA = {
        'first_name': 'Rado',
        'last_name': 'Hadzhiev',
        'age': 24,
    }

    def test_create_profile__when_all_valid__expect_to_create(self):

        self.client.post(
            reverse('create profile'),
            data=self.VALID_PROFILE_DATA,
        )

        # Take the profile from the DB
        profile = Profile.objects.get()
        self.assertIsNotNone(profile)
        self.assertEqual(self.VALID_PROFILE_DATA['first_name'], profile.first_name)
        self.assertEqual(self.VALID_PROFILE_DATA['last_name'], profile.last_name)
        self.assertEqual(self.VALID_PROFILE_DATA['age'], profile.age)

    #  Test redirects
    def test_create_profile__when_all_valid__expect_to_redirect(self):
        response = self.client.post(
            reverse('create profile'),
            data=self.VALID_PROFILE_DATA,
        )

        profile = Profile.objects.get()

        expected_url = reverse('details profile', kwargs={'pk': profile.pk})
        self.assertRedirects(response, expected_url)

    #  Test status code
