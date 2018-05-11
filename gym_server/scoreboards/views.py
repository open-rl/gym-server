# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from allauth.socialaccount.models import SocialAccount, SocialToken
from datetime import datetime
from environments.models import Environment
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from scoreboards.models import EvaluationRun
from scoreboards.serializers import EvaluationRunSerializer, ScoreBoardSerializer


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
    def get(self, request):
        if request.GET.get('token', None) is None:
            return Response({'error': 'auth token missing'},
                            status=status.HTTP_401_UNAUTHORIZED)

        auth_token = request.GET.get('token')

        # get social account
        try:
            account = SocialAccount.objects.get(socialtoken__token=auth_token)
        except SocialAccount.DoesNotExist:
            return Response({'error': 'no associated account found'},
                            status=status.HTTP_400_BAD_REQUEST)

        # build upload url: {social account uid}/eval_{datetime string}
        datetime_str = datetime.utcnow().strftime('%Y_%m_%d_%H_%M_%S')
        upload_path = '{}/eval_{}'.format(account.uid, datetime_str)

        # handle URL signing via boto3
