from allauth.socialaccount.models import SocialAccount
from authentication.models import AuthToken
from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import force_authenticate, APITestCase
from scoreboards.views import EvaluationRunViewSet, S3UploadURLView


class S3UploadURLViewTest(APITestCase):
    '''
    This test suite ensures that the `S3UploadURLView` works as follows:
    - In case the client is not authenticated, we reject the request
      sending an HTTP 401 response
    - In case the client is authenticated, but no user is associated with
      the current `SocialToken`, we respond with an HTTP 400 response
    - Else, we send an HTTP 200 response with an `url` key containing the
      url.
    '''
    def test_rejects_unauthenticated_user(self):
        resp = self.client.get('/url-sign-request/')
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_sends_400_if_user_not_found(self):
        resp = self.client.get('/url-sign-request/?token=test-test')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_url_signed_correctly_if_user_exists(self):
        account = mixer.blend(SocialAccount)
        token = mixer.blend(AuthToken, account=account.user)

        resp = self.client.get('/url-sign-request/?token={}'.format(token.token))
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(resp.data.get('url', None))
