from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from authentication.serializers import GithubLoginSerializer
from rest_auth.registration.views import SocialLoginView


class GithubLoginView(SocialLoginView):
    serializer_class = GithubLoginSerializer
    adapter_class = GitHubOAuth2Adapter
