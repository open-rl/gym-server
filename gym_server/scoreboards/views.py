# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from allauth.socialaccount.models import SocialAccount, SocialToken
from boto.s3.connection import S3Connection
from datetime import datetime
from django.conf import settings
from environments.models import Environment
import logging
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from scoreboards.models import EvaluationRun
from scoreboards.serializers import (EvaluationRunSerializer,
                                     S3UploadURLSerializer)


logger = logging.getLogger(__name__)


class EvaluationRunViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    The `EvaluationRunViewSet` provides `list` and `retrieve` functionality
    for the `EvaluationRun` model class.
    '''
    serializer_class = EvaluationRunSerializer
    queryset = EvaluationRun.objects.all()


class S3UploadURLView(APIView):
    '''
    This view is used by the client to retrieve a presigned upload URL,
    which it uses to upload its training evaluation to our bucket. Following our
    convention, our upload path inside the bucket is composed of the datetime string
    prefixed by the client uid.

    The actual signing is facilitated by the boto3 library, which provides
    this functionality out of the box. More, we do not need to pass in any
    credentials as we enable this functionality on an EC2 role basis.
    '''
    s3_connection = S3Connection()

    def get(self, request):
        logging.debug('Received upload request')
        if request.GET.get('token', None) is None:
            logging.debug('No token provided')
            return Response({'error': 'auth token missing'},
                            status=status.HTTP_401_UNAUTHORIZED)

        auth_token = request.GET.get('token')

        # get social account
        try:
            logging.debug('Fetching Social Account')
            account = SocialAccount.objects.get(socialtoken__token=auth_token)
        except SocialAccount.DoesNotExist:
            logging.debug('No matching social account found')
            return Response({'error': 'no associated account found'},
                            status=status.HTTP_400_BAD_REQUEST)

        # build upload url: {social account uid}/eval_{datetime string}
        datetime_str = datetime.utcnow().strftime('%Y_%m_%d_%H_%M_%S')
        key = '{}/eval_{}'.format(account.uid, datetime_str)

        # sign URL via boto
        url = self.s3_connection\
            .generate_url(3600, 'PUT', key=key, bucket=settings.S3_EVALUATION_BUCKET)

        # return serialized response
        serializer = S3UploadURLSerializer({'url': url})
        return Response(serializer.data)
