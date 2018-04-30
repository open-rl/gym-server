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


class ScoreBoardView(APIView):
    '''
    The `ScoreBoardView` implements a view to retrieve any given environment's
    current score board.
    '''
    def get(self, request, env=None, format='json'):
        # check if env exists
        if not Environment.objects.filter(name=env).exists():
            return Response({'error': 'environment not found.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # return queryset ordered wrt set high score
        queryset = EvaluationRun\
            .objects\
            .filter(env__name=env)\
            .order_by('-high_score')[:30]
        serializer = ScoreBoardSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
