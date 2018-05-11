from rest_framework import serializers
from scoreboards.models import EvaluationRun


class EvaluationRunSerializer(serializers.ModelSerializer):
    '''
    `ModelSerializer` for the `EvaluationRun` model class
    '''

    class Meta:
        model = EvaluationRun
        fields = ('pk', 'user', 'env', 's3_path', 'high_score')
        depth = 1


class S3UploadURLSerializer(serializers.Serializer):
    '''
    The `S3UploadURLSerializer` provides de/serializing functionality for the
    pre-signed upload URL we provide to each client.
    '''
    url = serializers.URLField(max_length=255, read_only=True)

    class Meta:
        model = EvaluationRun
        fields = ('pk', 'user', 's3_path', 'high_score')
