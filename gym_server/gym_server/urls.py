'''gym_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
'''
from django.conf.urls import include, url
from django.urls import re_path
from django.contrib import admin
from environments.views import EnvironmentViewSet
from rest_framework import routers
from scoreboards.views import EvaluationRunViewSet


# register environment router
environment_router = routers.SimpleRouter()
environment_router.register('', EnvironmentViewSet, base_name='environment')

# register evaluation router
eval_router = routers.SimpleRouter()
eval_router.register('', EvaluationRunViewSet, base_name='evaluation')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('authentication.urls')),
    url(r'^environments/', include(environment_router.urls)),
    url(r'^evaluations/', include(eval_router.urls)),
]
