#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

cfg = []
f = open("cfg.txt", "r")
for linea in f:
    cfg.append(linea)
f.close()
name_app = cfg[0]
name_enterprise = cfg[1]


urlpatterns = [
	path('', IndexView.as_view(), name='index'),
    path('upload', UploadView.as_view(), name='upload'),
    path('cache', CacheView.as_view(), name='cache'),
    path('settings', SettingsView.as_view(), name='settings'),
    path('files', ListDir.as_view(), name='list'),
    path('list/sheetnames', SheetsView.as_view(), name='sheets'),
    path('list/sheetnames/<str:file>', BackSheetsView.as_view(), name='backsheets'),
    path('read/sheet/columns/<str:file>', RsheetView.as_view(), name='rsheet'),
    path('read/<str:sheet>/<str:file>', RcsheetView.as_view(), name='rcsheet'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
