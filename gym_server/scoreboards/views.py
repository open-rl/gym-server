# -*- coding: utf-8 -*-
from __future__ import unicode_literals
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
