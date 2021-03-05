#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""▌ ▌      ▌        ▐  ▌
   ▙▄▌▌ ▌▞▀▌▛▀▖▛▀▖▌ ▌▜▀ ▛▀▖▞▀▖▛▀▖▞▀▖▞▀▖▙▀▖
   ▌ ▌▌ ▌▚▄▌▌ ▌▙▄▘▚▄▌▐ ▖▌ ▌▌ ▌▌ ▌▛▀ ▛▀ ▌
   ▘ ▘▝▀▘▗▄▘▘ ▘▌  ▗▄▘ ▀ ▘ ▘▝▀ ▘ ▘▝▀▘▝▀▘▘  2020"""

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView, View
from django.utils.decorators import method_decorator
from .models import *
import pandas as pd
from pyxlsb import convert_date
import datetime
from datetime import datetime
from .models import *
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from demo.settings import STATIC_ROOT, STATIC_URL
from django.core.files.storage import FileSystemStorage
import json
import re
import glob
import sys
import os.path
import time
from os import remove
import xlrd

# Create your views here.

"""
Hughpythoneer
@author Hugo Ramírez
@copyright Hughpythoneer
@cto Hughpythoneer
@date 01-06-2020
@version 2.0.0
"""

"""
Clase que controla el template Index y de no existir
ningun archivo en el directorio de trabajo envia un
mensaje comunicando el hecho de lo contrario
listara los archivos existentes en un campo de seleccion"""
class IndexView(TemplateView):
    """docstring for IndexView"""
    template_name = 'template.index.html'
    def dispatch(self, *args, **kwargs):
        cfg = []
        f = open("cfg.txt", "r")
        for linea in f:
            cfg.append(linea)
        f.close()
        name_app = cfg[0]
        name_enterprise = cfg[1]
        context = {'name_app': name_app, 'name_enterprise': name_enterprise}
        pwd = os.getcwd()
        path = '{}/static/media/'.format(pwd)
        files = {}
        with os.scandir(path) as ficheros:
            count = 0
            for fichero in ficheros:
                name = fichero.name
                count += 1
                files['file{}'.format(count)] = name
        if len(files) is 0:
            context = {'mensaje':'Need to upload files'}
            return super().dispatch(*args, **kwargs, **context)
        else:
            return redirect('list')

""""""
class UploadView(View):
    """docstring for UploadView"""
    template_name = 'template.upload.html'
    def get(self, request, *args, **kwargs):
        cfg = []
        f = open("cfg.txt", "r")
        for linea in f:
            cfg.append(linea)
        f.close()
        name_app = cfg[0]
        name_enterprise = cfg[1]
        context = {'name_app': name_app, 'name_enterprise': name_enterprise}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        uploaded_file = request.FILES['file']
        file, ext = os.path.splitext(str(uploaded_file))
        if ext == '.csv' or ext == '.xlsb' or ext == '.xlsm' or ext == '.xlsx':
            name = uploaded_file.name
            pwd = os.getcwd()
            path_true = pwd+'/static/media/'+name
            context = {}
            if os.path.exists(path_true):
                cfg = []
                f = open("cfg.txt", "r")
                for linea in f:
                    cfg.append(linea)
                f.close()
                name_app = cfg[0]
                name_enterprise = cfg[1]
                mensaje = 'the file already exists'
                context = {'mensaje': mensaje, 'name_app': name_app, 'name_enterprise': name_enterprise}
                return render(request, self.template_name, context)
            else:
                cfg = []
                f = open("cfg.txt", "r")
                for linea in f:
                    cfg.append(linea)
                f.close()
                name_app = cfg[0]
                name_enterprise = cfg[1]
                fs = FileSystemStorage(location='static/media')
                path_article = fs.save(uploaded_file.name, uploaded_file)
                context['url'] = fs.url(path_article)
                url = fs.url(path_article)
                mensaje = 'the file was successfully attached'
                context = {'mensaje': mensaje, 'name_app': name_app, 'name_enterprise': name_enterprise}
                return HttpResponseRedirect('files', context)
        else:
            mensaje = 'unsupported file'
            context = {'mensaje': mensaje}
            return render(request, self.template_name, context)

        #return redirect('upload')
        #return HttpResponseRedirect(reverser('upload', args=context))

class CacheView(View):
    template_name = 'template.index.html'
    def get(self, request, *args, **kwargs):
        try:
            cfg = []
            f = open("cfg.txt", "r")
            for linea in f:
                cfg.append(linea)
            f.close()
            name_app = cfg[0]
            name_enterprise = cfg[1]
            pwd = os.getcwd()
            path = pwd+'/static/media/*'
            files = glob.glob(path)
            for f in files:
                os.remove(f)
            mensaje = 'the cache has been freed'
            context = {'mensaje': mensaje, 'name_app': name_app, 'name_enterprise': name_enterprise}
            return render(request, self.template_name, context)
        except:
            cfg = []
            f = open("cfg.txt", "r")
            for linea in f:
                cfg.append(linea)
            f.close()
            name_app = cfg[0]
            name_enterprise = cfg[1]
            mensaje = 'the cache memory is already released'
            context = {'mensaje': mensaje, 'name_app': name_app, 'name_enterprise': name_enterprise}
            return render(request, self.template_name, context)


class SettingsView(View):
    template_name = 'template.settings.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        name_app= request.POST['name_app']
        name_enterprise = request.POST['name_enterprise']
        pwd = os.getcwd()
        f = open(pwd+"/cfg.txt", "w")
        f.write(str(name_app))
        f.write('\n' + str(name_enterprise))
        f.close()
        cfg = []
        f = open("cfg.txt", "r")
        for linea in f:
            cfg.append(linea)
        f.close()
        return render(request, self.template_name)


class ListDir(View):
    """docstring for ListDir"""
    template_name = 'template.index.html'
    def get(self, request):
        pwd = os.getcwd()
        path = '{}/static/media/'.format(pwd)
        contenido = os.listdir(pwd)
        files = {}
        with os.scandir(path) as ficheros:
            count = 0
            for fichero in ficheros:
                name = fichero.name
                count += 1
                files['file{}'.format(count)] = name

        cfg = []
        f = open("cfg.txt", "r")
        for linea in f:
            cfg.append(linea)
        f.close()
        name_app = cfg[0]
        name_enterprise = cfg[1]
        context = {'data': files, 'name_app': name_app, 'name_enterprise': name_enterprise}
        return render(request, self.template_name, context)

class SheetsView(View):
    """docstring for SheetsView"""
    template_name = 'template.sheets.html'
    def post(self, request):
        filename = request.POST['choosefile']
        pwd = os.getcwd()
        path = '{}/static/media/{}'.format(pwd, filename)
        file, ext = os.path.splitext(filename)
        if ext == '.xlsb':
            xls = pd.ExcelFile(path, engine='pyxlsb')
            sheets = xls.sheet_names
            names = {}
            count = 0
            for name in sheets:
                count += 1
                names['name{}'.format(count)] = name
            context = {'sheets':names, 'filename':filename}
            return render(request, self.template_name, context)

        elif ext == '.xlsm':
            xls = pd.ExcelFile(path)
            sheets = xls.sheet_names
            names = {}
            count = 0
            for name in sheets:
                count += 1
                names['name{}'.format(count)] = name
            context = {'sheets':names, 'filename':filename}
            return render(request, self.template_name, context)

        elif ext == '.xlsx':
            xls = pd.ExcelFile(path)
            sheets = xls.sheet_names
            names = {}
            count = 0
            for name in sheets:
                count += 1
                names['name{}'.format(count)] = name
            context = {'sheets':names, 'filename':filename}
            return render(request, self.template_name, context)

        elif ext == '.csv':
            cfg = []
            f = open("cfg.txt", "r")
            for linea in f:
                cfg.append(linea)
            f.close()
            name_app = cfg[0]
            sheet = filename.replace('.csv', '')
            names = {}
            names['name'] = sheet
            context = {'sheets':names, 'filename':filename, 'name_app':name_app}
            return render(request, self.template_name, context)

        else:
            return render(request, self.template_name)


class BackSheetsView(View):
    """docstring for SheetsView"""
    template_name = 'template.sheets.html'
    def get(self, request, file):
        filename = file
        pwd = os.getcwd()
        path = '{}/static/media/{}'.format(pwd, filename)
        file, ext = os.path.splitext(filename)
        if ext == '.xlsb':
            xls = pd.ExcelFile(path, engine='pyxlsb')
            sheets = xls.sheet_names
            names = {}
            count = 0
            for name in sheets:
                count += 1
                names['name{}'.format(count)] = name
            context = {'sheets':names, 'filename':filename}
            return render(request, self.template_name, context)

        elif ext == '.xlsm':
            xls = pd.ExcelFile(path)
            sheets = xls.sheet_names
            names = {}
            count = 0
            for name in sheets:
                count += 1
                names['name{}'.format(count)] = name
            context = {'sheets':names, 'filename':filename}
            return render(request, self.template_name, context)

        elif ext == '.xlsx':
            xls = pd.ExcelFile(path)
            sheets = xls.sheet_names
            names = {}
            count = 0
            for name in sheets:
                count += 1
                names['name{}'.format(count)] = name
            context = {'sheets':names, 'filename':filename}
            return render(request, self.template_name, context)

        elif ext == '.csv':
            cfg = []
            f = open("cfg.txt", "r")
            for linea in f:
                cfg.append(linea)
            f.close()
            name_app = cfg[0]
            sheet = filename.replace('.csv', '')
            names = {}
            names['name'] = sheet
            context = {'sheets':names, 'filename':filename, 'name_app':name_app}
            return render(request, self.template_name, context)

        else:
            return render(request, self.template_name)






class RsheetView(View):
    """docstring for RsheetView."""
    template_name = 'template.rsheets.html'
    def post(self, request, file):

        sheetname = request.POST['choosesheet']
        fl, ext = os.path.splitext(file)

        if ext == '.xlsb':
            pwd = os.getcwd()
            path = '{}/static/media/{}'.format(pwd, file)
            df = pd.read_excel(path, engine='pyxlsb', index_col=None, sheet_name=sheetname)
            columns = df.columns
            columns_dict = {}
            count = 0
            for name in columns:
                count += 1
                columns_dict['column{}'.format(count)] = name
            context = {'columns':columns_dict, 'filename':file, 'sheetname':sheetname}
            return render(request, self.template_name, context)

        if ext == '.xlsm':
            pwd = os.getcwd()
            path = '{}/static/media/{}'.format(pwd, file)
            df = pd.read_excel(path, index_col=None, sheet_name=sheetname)
            columns = df.columns
            columns_dict = {}
            count = 0
            for name in columns:
                count += 1
                columns_dict['column{}'.format(count)] = name
            context = {'columns':columns_dict, 'filename':file, 'sheetname':sheetname}
            return render(request, self.template_name, context)

        if ext == '.xlsx':
            pwd = os.getcwd()
            path = '{}/static/media/{}'.format(pwd, file)
            df = pd.read_excel(path, index_col=None, sheet_name=sheetname)
            columns = df.columns
            columns_dict = {}
            count = 0
            for name in columns:
                count += 1
                columns_dict['column{}'.format(count)] = name
            context = {'columns':columns_dict, 'filename':file, 'sheetname':sheetname}
            return render(request, self.template_name, context)

        if ext == '.csv':
            pwd = os.getcwd()
            path = '{}/static/media/{}'.format(pwd, file)
            df = pd.read_csv(path, index_col=None)
            columns = df.columns
            columns_dict = {}
            count = 0
            for name in columns:
                count += 1
                columns_dict['column{}'.format(count)] = name

            cfg = []
            f = open("cfg.txt", "r")
            for linea in f:
                cfg.append(linea)
            f.close()
            name_app = cfg[0]
            context = {'columns':columns_dict, 'filename':file, 'sheetname':sheetname, 'name_app':name_app}
            return render(request, self.template_name, context)

        else:
            return render(request, self.template_name)




"""DataTable a partir de un dataframe """
class RcsheetView(View):
    """docstring for RcsheetView."""
    template_name = 'template.rcsheets.html'
    def post(self, request, sheet, file):
        fl, ext = os.path.splitext(file)
        if ext == '.xlsb':
            pwd = os.getcwd()
            path = '{}/static/media/{}'.format(pwd, file)
            df = pd.read_excel(path, engine='pyxlsb', index_col=None, sheet_name=sheet)
            columns = df.columns
            dictcol = {}
            count = 0
            for name in columns:
                count += 1
                dictcol['column{}'.format(count)] = name
            lcolumns = []
            for i in range(1, len(dictcol)+1):
                try:
                    lcolumns.append(request.POST['column{}'.format(i)])
                except:
                    pass
            df = pd.read_excel(path, engine='pyxlsb', index_col=None, sheet_name=sheet, usecols=lcolumns)

            url = '{}/static/media/{}'.format('http://127.0.0.1:8000', file)

            class_bootstrap = ['table', 'table-striped', 'table-bordered', 'display', 'text-primary', 'h7']
            table = df.to_html(buf=None, columns=None, col_space=None, header=True, index=False, na_rep='NaN', formatters=None, float_format=None, sparsify=None, index_names=True, justify=None, max_rows=None, max_cols=None, show_dimensions=False, decimal='.', bold_rows=True, classes=class_bootstrap, escape=True, notebook=False, border=None, table_id='table_id', render_links=False, encoding=None)
            pwd = os.getcwd()
            template_file = open('{}/build/templates/template.table.html'.format(pwd), 'w')
            template_file.write(table)
            template_file.close()

            return render(request, self.template_name, {'url':url, 'filename':file, 'sheetname':sheet, 'lcolumns':lcolumns})

        if ext == '.xlsm':
            pwd = os.getcwd()
            path = '{}/static/media/{}'.format(pwd, file)
            df = pd.read_excel(path, index_col=None, sheet_name=sheet)
            columns = df.columns
            dictcol = {}
            count = 0
            for name in columns:
                count += 1
                dictcol['column{}'.format(count)] = name
            lcolumns = []
            for i in range(1, len(dictcol)+1):
                try:
                    lcolumns.append(request.POST['column{}'.format(i)])
                except:
                    pass
            df = pd.read_excel(path, index_col=None, sheet_name=sheet, usecols=lcolumns)


            url = '{}/static/media/{}'.format('http://127.0.0.1:8000', file)

            class_bootstrap = ['table', 'table-striped', 'table-bordered', 'display', 'text-primary', 'h7']
            table = df.to_html(buf=None, columns=None, col_space=None, header=True, index=False, na_rep='NaN', formatters=None, float_format=None, sparsify=None, index_names=True, justify=None, max_rows=None, max_cols=None, show_dimensions=False, decimal='.', bold_rows=True, classes=class_bootstrap, escape=True, notebook=False, border=None, table_id='table_id', render_links=False, encoding=None)
            pwd = os.getcwd()
            template_file = open('{}/build/templates/template.table.html'.format(pwd), 'w')
            template_file.write(table)
            template_file.close()

            return render(request, self.template_name, {'url':url, 'filename':file, 'sheetname':sheet, 'lcolumns':lcolumns})

        if ext == '.xlsx':
            pwd = os.getcwd()
            path = '{}/static/media/{}'.format(pwd, file)
            df = pd.read_excel(path, index_col=None, sheet_name=sheet)
            columns = df.columns
            dictcol = {}
            count = 0
            for name in columns:
                count += 1
                dictcol['column{}'.format(count)] = name
            lcolumns = []
            for i in range(1, len(dictcol)+1):
                try:
                    lcolumns.append(request.POST['column{}'.format(i)])
                except:
                    pass
            df = pd.read_excel(path, index_col=None, sheet_name=sheet, usecols=lcolumns)


            url = '{}/static/media/{}'.format('http://127.0.0.1:8000', file)

            class_bootstrap = ['table', 'table-striped', 'table-bordered', 'display', 'text-primary', 'h7']
            table = df.to_html(buf=None, columns=None, col_space=None, header=True, index=False, na_rep='NaN', formatters=None, float_format=None, sparsify=None, index_names=True, justify=None, max_rows=None, max_cols=None, show_dimensions=False, decimal='.', bold_rows=True, classes=class_bootstrap, escape=True, notebook=False, border=None, table_id='table_id', render_links=False, encoding=None)
            pwd = os.getcwd()
            template_file = open('{}/build/templates/template.table.html'.format(pwd), 'w')
            template_file.write(table)
            template_file.close()
            context = {'url':url, 'filename':file, 'sheetname':sheet, 'lcolumns':lcolumns}
            print(context)
            return render(request, self.template_name, context)

        if ext == '.csv':
            pwd = os.getcwd()
            path = '{}/static/media/{}'.format(pwd, file)
            df = pd.read_csv(path, index_col=None)
            columns = df.columns
            dictcol = {}
            count = 0
            for name in columns:
                count += 1
                dictcol['column{}'.format(count)] = name
            lcolumns = []
            for i in range(1, len(dictcol)+1):
                try:
                    lcolumns.append(request.POST['column{}'.format(i)])
                except:
                    pass

            df = pd.read_csv(path, index_col=None, usecols=lcolumns)
            url = '{}/static/media/{}'.format('http://127.0.0.1:8000', file)
            class_bootstrap = ['table', 'table-striped', 'table-bordered', 'display', 'text-primary', 'h7']
            table = df.to_html(buf=None, columns=None, col_space=None, header=True, index=False, na_rep='NaN', formatters=None, float_format=None, sparsify=None, index_names=True, justify=None, max_rows=None, max_cols=None, show_dimensions=False, decimal='.', bold_rows=True, classes=class_bootstrap, escape=True, notebook=False, border=None, table_id='table_id', render_links=False, encoding=None)
            pwd = os.getcwd()
            template_file = open('{}/build/templates/template.table.html'.format(pwd), 'w')
            template_file.write(table)
            template_file.close()

            return render(request, self.template_name, {'url':url, 'filename':file, 'sheetname':sheet, 'lcolumns':lcolumns})

        return render(request, self.template_name)
