#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from django.urls import path
from .views import *

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
    path('/dataframe', DataFrameView.as_view(), name='dataframe'),
]
