from authentication.utils import generate_unique_auth_token
from authentication.models import AuthToken
from django.test import TestCase
from mock import patch


def return_mock_token():
    return 'some-unique-string'


class AuthTokenGeneratorTest(TestCase):
    '''
    Here, we test our `generate_unique_auth_token` function, which handles
    creating a unique auth token represented by a hexadecimal string of size 16.
    '''
    def test_no_token_exists(self):
        token = generate_unique_auth_token()
        self.assertIsInstance(token, str)
        self.assertEqual(len(token), 40)

    @patch('authentication.utils.AuthToken.objects.get',
           side_effect=[return_mock_token, AuthToken.DoesNotExist])
    def test_recursive_call_if_token_exists(self, mock_token):
        token = generate_unique_auth_token()
        self.assertIsInstance(token, str)
        self.assertEqual(len(token), 40)
