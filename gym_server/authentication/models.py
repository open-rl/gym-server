from django.contrib.auth.models import User
from django.db import models


class AuthToken(models.Model):
    '''
    The `AuthToken` model represents a simple token, which gets automatically
    generated when a new user signs up. It is then used to authenticate this
    user, whenever he or she uploads an evaluation to our S3 bucket.

    The reason not to use the users `SocialToken` from allauth is that this may
    be used to extract all personal information from github.
    '''
    account = models.OneToOneField(User, related_name='openrl_token',
                                   on_delete=models.CASCADE)
    token = models.CharField(max_length=255, blank=False, null=False,
                             default='test-token')
