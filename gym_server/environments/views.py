# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from environments.models import Environment
from environments.serializers import EnvironmentSerializer
from rest_framework import viewsets
from rest_framework.exceptions import ParseError
from rest_framework.response import Response


class EnvironmentViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    The `EnvironmentViewSet` provides `list` and `retrieve` functionality
    for the `Environment` model class.
    '''
    serializer_class = EnvironmentSerializer
    queryset = Environment.objects.all()
