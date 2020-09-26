from django.shortcuts import render

# Create your views here.

"""▐                       ▐   ▜▘      
   ▜▀ ▞▀▖▞▀▘▞▀▘▞▀▖▙▀▖▝▀▖▞▀▖▜▀  ▐ ▛▀▖▞▀▖
   ▐ ▖▛▀ ▝▀▖▝▀▖▛▀ ▌  ▞▀▌▌ ▖▐ ▖ ▐ ▌ ▌▌ ▖
    ▀ ▝▀▘▀▀ ▀▀ ▝▀▘▘  ▝▀▘▝▀  ▀  ▀▘▘ ▘▝▀  2020"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
import pandas as pd
from pyxlsb import convert_date
import datetime

#https://docs.djangoproject.com/en/3.0/topics/class-based-views/intro/
# Create your views here.

"""
Tesseract Inc
@author Ing. Alejandro Ramírez
@copyright Tesseract Inc
@cto Tesseract Inc
@date 01-09-2020
@version 2.0.0
"""

class ClassName(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg
        
class IndexView(TemplateView):
    """docstring for tesseractView"""
    template_name = 'template.index.html'
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    
class DataFrameView(View):
    template_name = 'template.dataframe.html'
    def get(self, request, *args, **kwargs):
        atributos = ['Codigo de Entrega', 'Numero Serie', 'Fuente', 
            'Pais','Codigo de Cliente', 'Nombre cliente', 
             'Dirección', 'Distrito', 'Activo', 'Tamaño', 
             'Imagen/Publicidad', 'Año Fabricación', 'Fecha Instalación', 'Propiedad']
        df = pd.read_excel('parquefrio.xlsb', engine='pyxlsb', sheet_name='INSTALADO', usecols=atributos)
        unique_date = df['Fecha Instalación'].fillna(0, inplace=True)
        unique_date = df['Fecha Instalación'].dropna()
        date = []
        for i in unique_date:
            objeto = convert_date(i)
            objeto = pd.to_datetime(objeto, format=('%d/%m/%Y'))
            objeto.to_pydatetime()
            date.append(objeto)
        context = {'Fecha':date}
        return render(self.template_name, context)
    
    
    
    
"""class ContactFormView(View):
    form_class = ContactForm
    initial = {'key': 'value'}
    template_name = 'form_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})"""