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


class ScoreBoardSerializer(serializers.ModelSerializer):
    '''
    This class implements the `ModelSerializer` for the gym-server scoreboard.
    Basically, it is a `EvaluationRunSerializer` with modified fields, as we don't
    need to send along the `env` field with every request.
    '''
    class Meta:
        model = EvaluationRun
        fields = ('pk', 'user', 's3_path', 'high_score')
