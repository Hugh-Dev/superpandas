#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

settings_sheets = []
f = open("settings_sheets.txt", "r")
for linea in f:
    settings_sheets.append(linea)
f.close()
sheet_1 = settings_sheets[0]
sheet_2 = settings_sheets[1]
sheet_3 = settings_sheets[2]


urlpatterns = [
	path('', IndexView.as_view(), name='index'),
    path('sheet1', Sheet1View.as_view(), name='sheet_1'),
    path('cleaner', CleanerView.as_view(), name='cleaner'),
    path('upload', UploadView.as_view(), name='upload'),
    path('cache', CacheView.as_view(), name='cache'),
    path('sheet2', Sheet2View.as_view(), name='sheet_2'),
	path('sheet3', Sheet3View.as_view(), name='sheet_3'),
	path('context', ContextView.as_view(), name='context'),
    path('settings', SettingsView.as_view(), name='settings'),
    path('sheet3/<int:id>', Edit3View.as_view(), name='sheet3-edit'),
    path('list', ListDir.as_view(), name='list'),
    path('file', SheetsView.as_view(), name='sheets'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
