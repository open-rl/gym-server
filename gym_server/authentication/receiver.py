from allauth.socialaccount.signals import social_account_added
from authentication.models import AuthToken
from authentication.utils import generate_unique_auth_token


def generate_auth_token(request, sociallogin, **kwargs):
    '''
    This function picks up on the `allauth.socialaccount.signals.social_account_added`
    signal and generates a new auth token for the user. This is facilitated by
    hashing the user's username and the account creation time.
    '''
    account = sociallogin.user.user
    token = generate_unique_auth_token()

    AuthToken.objects.create(account=account, token=token)


social_account_added.connect(generate_auth_token, dispatch_uid='generate_token')
