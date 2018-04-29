from rest_framework import serializers
from environments.models import Environment


class EnvironmentSerializer(serializers.ModelSerializer):
    '''
    `ModelSerializer` for the `Environment` model class
    '''

    class Meta:
        model = Environment
        fields = ('pk', 'name', 'description', 'video_url')
