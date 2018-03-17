"""Doger URL Configuration

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
"""
from django.conf.urls import include, url
from django.contrib import admin
from api.views import *

urlpatterns = [
    url(r'^goods/(?P<gid>(\d)+)/$', GoodsView.as_view()),
    url(r'^goods/$', GoodsListView.as_view()),
    url(r'^user/$', UserInfoView.as_view()),
    url(r'^user/pet/$', PetUserInfo.as_view()),
    url(r'^gifts/$', GiftListView.as_view()),
    url(r'^pet/action/$', PetServiceView.as_view()),
    url(r'^pick/$', ShitView.as_view()),
    url(r'^encounters/$', EncounterListView.as_view()),
    url(r'^encounter/(?P<mid>(\d)+)/$', EncounterView.as_view()),
]
