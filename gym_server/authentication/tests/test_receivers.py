from authentication.receiver import generate_auth_token
from authentication.models import AuthToken
from django.contrib.auth.models import User
from django.test import TestCase
from mixer.backend.django import mixer
from mock import MagicMock


class GenerateAuthTokenTest(TestCase):
    '''
    This test suite covers the necessary tests for `receiver.generate_auth_token`,
    which is invoked by the `allauth.socialaccount.signals.social_account_added`
    signal. We need to ensure that we create a new `AuthToken` instance for any
    new user created.
    '''
    def test_correct_auth_token_creation(self):
        user = mixer.blend(User)

        social_login = MagicMock()
        social_login.user = user

        generate_auth_token(MagicMock(), social_login)

        self.assertIsInstance(user.openrl_token, AuthToken)
        self.assertEqual(user.openrl_token.account, user)
