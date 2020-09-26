#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
    path('dataframe', DataFrameView.as_view(), name='dataframe'),
    path('cleaner', CleanerView.as_view(), name='cleaner'),
    path('adjuntar', AdjuntarView.as_view(), name='adjuntar'),
    path('cache', CacheView.as_view(), name='cache'),
    path('bodega', BodegaView.as_view(), name='bodega'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)