from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.conf import settings
from rest_auth.registration.serializers import SocialLoginSerializer
from rest_auth.registration.views import SocialLoginView


class GithubLoginView(SocialLoginView):
    serializer_class = SocialLoginSerializer
    adapter_class = GitHubOAuth2Adapter
    client_class = OAuth2Client
    callback_url = settings.AUTH_CALLBACK_URL
