# Wrong
from django.contrib.auth.models import User

# Correct
from django.contrib.auth import get_user_model

UserModel = get_user_model()
# print(UserModel == User)
# pesho = UserModel(username='pesho_mashinata')
# pesho.set_password('123')  # Django stores all password using One way Hash
UserModel.objects.create_user(
    username='pesho_mashinata',
    password='123QwER',
)
