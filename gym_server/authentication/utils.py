from authentication.models import AuthToken
import binascii
import os


def generate_unique_auth_token():
    '''
    This function generates a unique auth token for our users whenever a new
    account is created. The function is implemented recursively, returning a
    call to itself, whenever a generated auth token already exists
    (highly unlikely though :P)
    '''
    token = binascii.hexlify(os.urandom(20)).decode()
    try:
        AuthToken.objects.get(token=token)
        return generate_unique_auth_token()
    except AuthToken.DoesNotExist:
        return token
