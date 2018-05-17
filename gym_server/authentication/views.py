from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from rest_auth.registration.serializers import SocialLoginSerializer
from rest_auth.registration.views import SocialLoginView


class GithubLoginView(SocialLoginView):
    serializer_class = SocialLoginSerializer
    adapter_class = GitHubOAuth2Adapter
