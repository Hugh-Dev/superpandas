from django.shortcuts import render

# Create your views here.

"""▐                       ▐   ▜▘      
   ▜▀ ▞▀▖▞▀▘▞▀▘▞▀▖▙▀▖▝▀▖▞▀▖▜▀  ▐ ▛▀▖▞▀▖
   ▐ ▖▛▀ ▝▀▖▝▀▖▛▀ ▌  ▞▀▌▌ ▖▐ ▖ ▐ ▌ ▌▌ ▖
    ▀ ▝▀▘▀▀ ▀▀ ▝▀▘▘  ▝▀▘▝▀  ▀  ▀▘▘ ▘▝▀  2020"""

from django.shortcuts import render, redirect
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
from demo.settings import STATIC_ROOT, STATIC_URL 
from django.core.files.storage import FileSystemStorage
import re
import sys
import os.path
from os import remove

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
    """docstring for IndexView"""
    template_name = 'template.index.html'
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    
class DataFrameView(View):
    template_name = 'template.dataframe.html'
    def get(self, request, *args, **kwargs):
        count = DataFrameModel.objects.count()
        if count == 0:
            try:
                atributos = ['Codigo de Entrega', 'Numero Serie', 'Fuente', 
                'Pais','Codigo de Cliente', 'Nombre cliente', 
                'Dirección', 'Distrito', 'Activo', 'Tamaño', 
                'Imagen/Publicidad', 'Año Fabricación', 'Fecha Instalación', 'Propiedad']
                pwd = os.getcwd()
                df = pd.read_excel(pwd+'/static/media/parquefrio.xlsb', engine='pyxlsb', sheet_name='INSTALADO', usecols=atributos)
                
                unique_date = df['Fecha Instalación'].fillna(0)

                dataframe = df.iloc[14567:20000]


                unique_date = dataframe['Fecha Instalación'].fillna(0)
                date = []
                for i in unique_date:
                    objeto = convert_date(i)
                    objeto = pd.to_datetime(objeto, format=('%d/%m/%Y'))
                    date.append(objeto)
                
                
                result = []
                for target_list in date:
                    objeto = target_list.strftime("%Y-%m-%d")
                    result.append(objeto)
                    
                
                unique_codigo = dataframe['Codigo de Entrega']
                codigo = []
                for target_list in unique_codigo:
                    codigo.append(target_list)

                
                unique_serie = dataframe['Numero Serie']
                serie = []
                for target_list in unique_serie:
                    serie.append(target_list)


                unique_fuente = dataframe['Fuente']
                fuente = []
                for target_list in unique_fuente:
                    fuente.append(target_list)

                unique_pais = dataframe['Pais']
                pais = []
                for target_list in unique_pais:
                    pais.append(target_list)
                

                unique_nombre = dataframe['Nombre cliente']
                nombre = []
                for target_list in unique_nombre:
                    nombre.append(target_list)

                unique_direccion = dataframe['Dirección']
                direccion = []
                for target_list in unique_direccion:
                    direccion.append(target_list)

                unique_distrito = dataframe['Distrito']
                distrito = []
                for target_list in unique_distrito:
                    distrito.append(target_list)
                

                unique_activo = dataframe['Activo']
                activo = []
                for target_list in unique_activo:
                    activo.append(target_list)


                unique_tamaño = dataframe['Tamaño']
                tamaño = []
                for target_list in unique_tamaño:
                    tamaño.append(target_list)

                unique_imagen = dataframe['Imagen/Publicidad']
                imagen = []
                for target_list in unique_imagen:
                    imagen.append(target_list)

                unique_año = dataframe['Año Fabricación']
                año = []
                for target_list in unique_año:
                    año.append(target_list)

                unique_fecha = dataframe['Fecha Instalación']
                fecha = []
                for target_list in unique_fecha:
                    fecha.append(target_list)

                unique_propiedad = dataframe['Propiedad']
                propiedad = []
                for target_list in unique_propiedad:
                    propiedad.append(target_list)


                unique_cliente = dataframe['Codigo de Cliente']
                cliente = []
                for target_list in unique_cliente:
                    cliente.append(target_list)

                for i in range(len(codigo)):
                    obj = DataFrameModel.objects.create(codigo=codigo[i], serie=serie[i], fuente=fuente[i], pais=pais[i], cliente=cliente[i], nombre=nombre[i], direccion=direccion[i], distrito=distrito[i], activo=activo[i], imagen=imagen[i], año=año[i], fecha=result[i], propiedad=propiedad[i], tamaño=tamaño[i])
                    obj.save()
                    

                choices = DataFrameModel.objects.all()
                context = {'choices':choices}
                return render(request, self.template_name, context)
            except:
                mensaje = 'No existe un archivo adjunto'
                context = {'mensaje': mensaje}
                return render(request, self.template_name, context)
        
        else:
            mensaje = 'La memoria esta llena'
            context = {'mensaje': mensaje}
            return render(request, self.template_name, context) 

        
    

class CleanerView(View):
    template_name = 'template.index.html'
    def get(self, request, *args, **kwargs):
        Cleaner = DataFrameModel.objects.all()
        Cleaner.delete()
        mensaje = 'Los marcos de datos han sido eliminados'
        context = {'mensaje': mensaje}
        return render(request, self.template_name, context)


class AdjuntarView(View):
    template_name = 'template.adjuntar.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        uploaded_file = request.FILES['file']
        name = uploaded_file.name
        pwd = os.getcwd()
        path_true = pwd+'/static/media/'+name
        context = {}
        if os.path.exists(path_true):
            mensaje = 'El archivo ya existe'
            context = {'mensaje': mensaje}
            return render(request, self.template_name, context)
        else:
            fs = FileSystemStorage(location='static/media')
            path_article = fs.save(uploaded_file.name, uploaded_file)
            context['url'] = fs.url(path_article)
            url = fs.url(path_article)
            mensaje = 'El archivo fue adjuntado con exito'
            context = {'mensaje': mensaje}
            return render(request, self.template_name, context)
    
        return redirect('adjuntar')


class CacheView(View):
    template_name = 'template.index.html'
    def get(self, request, *args, **kwargs):

        try:
            pwd = os.getcwd()
            remove(pwd+'/static/media/parquefrio.xlsb')
            mensaje = 'La memoria cache limpia'
            context = {'mensaje': mensaje}
            return render(request, self.template_name, context)
        except:
            mensaje = 'La memoria cache ya esta vacia'
            context = {'mensaje': mensaje}
            return render(request, self.template_name, context)
        

class BodegaView(View):
    template_name = 'template.bodega.html'
    def get(self, request, *args, **kwargs):
        try:
            atributos = ['Fuente', 'CSD/CVZ', 'Pais', 
                'Cet','Nombre Cet', 'Ruta', 
                'Frec.', 'Codigo de Cliente', 'Nombre cliente', 'Dirección', 
                'Distrito', 'Distrito 2', 'OfVta', 'Oficina de ventas', 'Material',
                 'Numero Serie', 'Activo Fijo', 'Imagen/Publicidad', 'Año Fabricación',
                  'Ingreso taller', 'Propiedad', 'Tamaño']
            pwd = os.getcwd()
            df = pd.read_excel(pwd+'/static/media/parquefrio.xlsb', engine='pyxlsb', sheet_name='BODEGA')
            #print(df.dtypes)
            #print(df.shape)
            #print(df['Ingreso taller'].fillna(0))
            #df = df.iloc[:]

            unique_ingreso_taller = df['Ingreso taller'].fillna(0)
            ingreso_taller = []
            for i in unique_ingreso_taller:
                objeto = convert_date(i)
                objeto = pd.to_datetime(objeto, format=('%d/%m/%Y'))
                ingreso_taller.append(objeto)

            fecha_ingreso_taller = []
            for target_list in ingreso_taller:
                objeto = target_list.strftime("%Y-%m-%d")
                fecha_ingreso_taller.append(objeto)
            

            unique_fuente = df['Fuente']
            fuente = []
            for target_list in unique_fuente:
                fuente.append(target_list)


            unique_csd_cvz = df['CSD/CVZ']

            csd_cvz = []
            for target_list in unique_csd_cvz:
                csd_cvz.append(target_list)

            unique_pais = df['Pais']
            pais = []
            for target_list in unique_pais:
                pais.append(target_list)

            unique_cet = df['Cet']
            cet = []
            for target_list in unique_cet:
                cet.append(target_list)

            unique_nombre_cet = df['Nombre Cet']
            nombre_cet = []
            for target_list in unique_nombre_cet:
                nombre_cet.append(target_list)

            unique_ruta = df['Ruta']
            ruta = []
            for target_list in unique_ruta:
                ruta.append(target_list)

            unique_frec = df['Frec.'] #.fillna(0)
            frec = []
            for target_list in unique_frec:
                frec.append(target_list)

            unique_codigo = df['Codigo de Cliente']
            codigo = []
            for target_list in unique_codigo:
                codigo.append(target_list)

            unique_nombre = df['Nombre cliente']
            nombre = []
            for target_list in unique_nombre:
                nombre.append(target_list)

            unique_direccion = df['Dirección']
            direccion = []
            for target_list in unique_direccion:
                direccion.append(target_list)

            unique_distrito = df['Distrito']
            distrito = []
            for target_list in unique_distrito:
                distrito.append(target_list)

            unique_distrito2 = df['Distrito 2']
            distrito2 = []
            for target_list in unique_distrito2:
                distrito2.append(target_list)

            unique_ofvta = df['OfVta']
            ofvta = []
            for target_list in unique_ofvta:
                ofvta.append(target_list)

            unique_oficina_ventas = df['Oficina de ventas']
            oficina_ventas = []
            for target_list in unique_oficina_ventas:
                oficina_ventas.append(target_list)

            unique_material = df['Material']
            material = []
            for target_list in unique_material:
                material.append(target_list)

            unique_serie = df['Numero Serie']
            serie = []
            for target_list in unique_serie:
                serie.append(target_list)

            unique_activo = df['Activo Fijo']
            activo = []
            for target_list in unique_activo:
                activo.append(target_list)

            unique_imagen = df['Imagen/Publicidad']
            imagen = []
            for target_list in unique_imagen:
                imagen.append(target_list)

            unique_año = df['Año Fabricación']
            año = []
            for target_list in unique_año:
                año.append(target_list)
            
            
            unique_prpiedad = df['Propiedad']
            propiedad = []
            for target_list in unique_prpiedad:
                propiedad.append(target_list)
            
            unique_tamaño = df['Tamaño']
            tamaño = []
            for target_list in unique_tamaño:
                tamaño.append(target_list)
            
            for i in range(len(codigo)):
                obj = BodegaModel.objects.create(csd_cvz=csd_cvz[i], cet=cet[i], nombre_cet=nombre_cet[i], frec=frec[i], ofvta=ofvta[i], oficina_ventas=oficina_ventas[i], material=material[i], codigo=codigo[i], serie=serie[i], fuente=fuente[i], pais=pais[i], ruta=ruta[i], nombre=nombre[i], direccion=direccion[i], distrito=distrito[i], distrito2=distrito2[i], activo=activo[i], tamaño=tamaño[i], imagen=imagen[i], año=año[i], fecha_ingreso_taller=fecha_ingreso_taller[i], propiedad=propiedad[i])
                print(obj)
                #obj.save()

            choices = BodegaModel.objects.all()
            context = {'choices':choices}
            return render(request, self.template_name, context)
        except:
            print('he are')
            return redirect('index')