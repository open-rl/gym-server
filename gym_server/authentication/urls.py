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
from allauth.account.views import confirm_email
from authentication.views import GithubLoginView
from django.conf.urls import url, include

urlpatterns = [
    url(r'github/$', GithubLoginView.as_view(), name='github_login'),
    url(r"^confirm-email/(?P<key>[-:\w]+)/$", confirm_email,
        name="account_confirm_email"),
    url(r'', include('rest_auth.urls')),
]
