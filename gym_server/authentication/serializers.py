from rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class OpenRLAccountSerializer(UserDetailsSerializer):
    '''
    Adds `auth_token` field to `SocialAccountSerializer`
    '''
    auth_token = serializers.ReadOnlyField(source='openrl_token.token')

    class Meta:
        model = UserDetailsSerializer.Meta.model
        fields = UserDetailsSerializer.Meta.fields + ('auth_token',)
