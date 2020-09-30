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
import time
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
        Cleaner_Bodega = BodegaModel.objects.all()
        Cleaner_Cloud = CloudModel.objects.all()
        Cleaner.delete()
        Cleaner_Bodega.delete()
        Cleaner_Cloud.delete()
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
        count = BodegaModel.objects.count()
        if count == 0:
            try:
                atributos = ['Fuente', 'CSD/CVZ', 'Pais',
                    'Cet','Nombre Cet', 'Ruta',
                    'Frec.', 'Codigo de Cliente', 'Nombre cliente', 'Dirección',
                    'Distrito', 'Distrito 2', 'OfVta', 'Oficina de ventas', 'Material',
                     'Numero Serie', 'Activo Fijo', 'Imagen/Publicidad', 'Año Fabricación',
                      'Ingreso taller', 'Propiedad', 'Tamaño']
                pwd = os.getcwd()
                df = pd.read_excel(pwd+'/static/media/parquefrio.xlsb', engine='pyxlsb', sheet_name='BODEGA', usecols=atributos)
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

                unique_pais = df['Pais'].fillna(0)
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

                unique_ruta = df['Ruta'].fillna(0)
                ruta = []
                for target_list in unique_ruta:
                    ruta.append(target_list)


                unique_frec = df['Frec.']
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
                    obj.save()

                choices = BodegaModel.objects.all()
                context = {'choices':choices}
                return render(request, self.template_name, context)
            except:
                print('he are')
                return redirect('index')
        else:
            mensaje = 'La memoria esta llena'
            context = {'mensaje': mensaje}
            return render(request, self.template_name, context)

class CloudView(View):
    """docstring for CloudView."""
    template_name = 'template.cloud.html'
    def get(self, request, *args, **kwargs):
        count = CloudModel.objects.count()
        if count == 0:
            try:
                atributos = ['N° de Serie', 'PROVEEDOR', 'PLAN', 'DÍAS SIN PROGRAMAR', 'PRIORIDAD', 'MOVIMIENTOS', 'TIPO DE SERVICIO', 'FECHA RECEPCIÓN', 'CODIGO DE CLIENTE', 'SALA DE VENTAS', 'Columna1', 'MESA', 'RUTA', 'Nombre del negocio / Cliente', 'Calle/ Dirección', 'Colonia, Barrio / Distrito', 'Departamento', 'Referencia como  llegar', 'RUC / DNI', 'PERSONA DE CONTACTO', 'Teléfono(s) de contacto', 'Horario de atención pdv', 'Modelo EF', 'LOGO', 'Tamaño', 'N° de Activo', 'Status Validación', 'Fecha Validación', 'Motivo del Rechazo', 'Explicación del Rechazo', 'Bonificación', 'PROCESO EJECUCIÓN', 'Fecha de Ejecución']                              
                pwd = os.getcwd()
                df = pd.read_excel(pwd+'/static/media/parquenube.xlsm', usecols=atributos) #, engine='', sheet_name='')
                

                """N° de Serie"""
                unique_serie = df['N° de Serie']
                serie = []
                for target_list in unique_serie:
                    serie.append(target_list)

                """PROVEEDOR"""
                unique_proveedor = df['PROVEEDOR']
                proveedor = []
                for target_list in unique_proveedor:
                    proveedor.append(target_list)

                """PLAN"""
                unique_plan = df['PLAN']
                plan = []
                for target_list in unique_plan:
                    plan.append(target_list)

                """DÍAS SIN PROGRAMAR"""
                unique_dias = df['DÍAS SIN PROGRAMAR']
                dias = []
                for target_list in unique_dias:
                    dias.append(target_list)

                """PRIORIDAD"""
                unique_prioridad = df['PRIORIDAD']
                prioridad = []
                for target_list in unique_prioridad:
                    prioridad.append(target_list)

                """MOVIMIENTOS"""
                unique_movimientos = df['MOVIMIENTOS']
                movimientos = []
                for target_list in unique_movimientos:
                    movimientos.append(target_list)

                
                """TIPO DE SERVICIO"""
                unique_tipo_servicio = df['TIPO DE SERVICIO']
                tipo_servicio = []
                for target_list in unique_tipo_servicio:
                    tipo_servicio.append(target_list)

                """FECHA RECEPCIÓN"""
                unique_fecha_recepcion = df['FECHA RECEPCIÓN']
                fecha_recepcion = []
                for target_list in unique_fecha_recepcion:
                    fecha_recepcion.append(target_list)

                fecha_recepcion_str = []
                for target_list in fecha_recepcion:
                    objeto = target_list.strftime("%Y-%m-%d")
                    fecha_recepcion_str.append(objeto)


                """CODIGO DE CLIENTE"""
                unique_codigo_cliente = df['CODIGO DE CLIENTE']
                codigo_cliente = []
                for target_list in unique_codigo_cliente:
                    codigo_cliente.append(target_list)

                """SALA DE VENTAS"""
                unique_sala_ventas = df['SALA DE VENTAS']
                sala_ventas = []
                for target_list in unique_sala_ventas:
                    sala_ventas.append(target_list)

                """Columna1"""
                unique_columna1 = df['Columna1']
                columna1 = []
                for target_list in unique_columna1:
                    columna1.append(target_list)

                """MESA"""
                unique_mesa = df['MESA']
                mesa = []
                for target_list in unique_mesa:
                    mesa.append(target_list)

                """RUTA"""
                unique_ruta = df['RUTA']
                ruta = []
                for target_list in unique_ruta:
                    ruta.append(target_list)

                """Nombre del negocio / Cliente"""
                unique_nombre_cliente = df['Nombre del negocio / Cliente']
                nombre_cliente = []
                for target_list in unique_nombre_cliente:
                    nombre_cliente.append(target_list)

                """Calle/ Dirección"""
                unique_nombre_calle_direccion = df['Calle/ Dirección']
                nombre_calle_direccion = []
                for target_list in unique_nombre_calle_direccion:
                    nombre_calle_direccion.append(target_list)

                """Colonia, Barrio / Distrito"""
                unique_colonia_barrio_distrito = df['Colonia, Barrio / Distrito']
                colonia_barrio_distrito = []
                for target_list in unique_colonia_barrio_distrito:
                    colonia_barrio_distrito.append(target_list)

                """Departamento"""
                unique_departamento = df['Departamento']
                departamento = []
                for target_list in unique_departamento:
                    departamento.append(target_list)

                """Referencia como  llegar"""
                unique_referencia = df['Referencia como  llegar']
                referencia = []
                for target_list in unique_referencia:
                    referencia.append(target_list)

                """RUC / DNI"""
                unique_dni_ruc = df['RUC / DNI']
                dni_ruc = []
                for target_list in unique_dni_ruc:
                    dni_ruc.append(target_list)

                """PERSONA DE CONTACTO"""
                unique_contacto = df['PERSONA DE CONTACTO']
                contacto = []
                for target_list in unique_contacto:
                    contacto.append(target_list)

                """Teléfono(s) de contacto"""
                unique_telefono = df['Teléfono(s) de contacto']
                telefono = []
                for target_list in unique_telefono:
                    telefono.append(target_list)

                """Horario de atención pdv"""
                unique_horario_atencion = df['Horario de atención pdv']
                horario_atencion = []
                for target_list in unique_horario_atencion:
                    horario_atencion.append(target_list)

                """Modelo EF"""
                unique_modelo_ef = df['Modelo EF']
                modelo_ef = []
                for target_list in unique_modelo_ef:
                    modelo_ef.append(target_list)

                """LOGO"""
                unique_logo = df['LOGO']
                logo = []
                for target_list in unique_logo:
                    logo.append(target_list)

                """Tamaño"""
                unique_tamaño = df['Tamaño']
                tamaño = []
                for target_list in unique_tamaño:
                    tamaño.append(target_list)

                """N° de Activo"""
                unique_activo = df['N° de Activo']
                activo = []
                for target_list in unique_activo:
                    activo.append(target_list)

                """Status Validación"""
                unique_status_validacion = df['Status Validación']
                status_validacion = []
                for target_list in unique_status_validacion:
                    status_validacion.append(target_list)

                """Fecha Validación"""
                unique_fecha_validacion = df['Fecha Validación'].fillna(0)
                fecha_validacion = []
                for target_list in unique_fecha_validacion:
                    fecha_validacion.append(target_list)

                validacion = []
                for i in fecha_validacion:
                    objeto = pd.to_datetime(i)
                    validacion.append(objeto)

                fecha_validacion_str = []
                for i in range(len(validacion)):
                    obj = validacion[i].strftime("%Y-%m-%d")
                    fecha_validacion_str.append(obj)



                """Motivo del Rechazo"""
                unique_motivo_rechazo = df['Motivo del Rechazo']
                motivo_rechazo = []
                for target_list in unique_motivo_rechazo:
                    motivo_rechazo.append(target_list)


                """Explicación del Rechazo"""
                unique_explicacion_rechazo = df['Explicación del Rechazo']
                explicacion_rechazo = []
                for target_list in unique_explicacion_rechazo:
                    explicacion_rechazo.append(target_list)


                """Bonificación"""
                unique_bonificacion = df['Bonificación']
                bonificacion = []
                for target_list in unique_bonificacion:
                    bonificacion.append(target_list)


                """PROCESO EJECUCIÓN"""
                unique_proceso_ejecucion = df['PROCESO EJECUCIÓN']
                proceso_ejecucion = []
                for target_list in unique_proceso_ejecucion:
                    proceso_ejecucion.append(target_list)


                """Fecha de Ejecución"""
                unique_fecha_ejecucion = df['Fecha de Ejecución'].fillna(0)
                fecha_ejecucion = []
                for target_list in unique_fecha_ejecucion:
                    fecha_ejecucion.append(target_list)

                ejecucion = []
                for i in fecha_ejecucion:
                    objeto = pd.to_datetime(i)
                    ejecucion.append(objeto)

                fecha_ejecucion_str = []
                for i in range(len(ejecucion)):
                    objeto = ejecucion[i].strftime("%Y-%m-%d")
                    fecha_ejecucion_str.append(objeto)

                for i in range(len(codigo_cliente)):
                    cloud = CloudModel.objects.create(serie=serie[i], proveedor=proveedor[i], plan=plan[i], dias=dias[i], prioridad=prioridad[i], movimientos=movimientos[i], tipo_servicio=tipo_servicio[i], fecha_recepcion=fecha_recepcion_str[i], codigo_cliente=codigo_cliente[i], sala_ventas=sala_ventas[i], columna1=columna1[i], mesa=mesa[i], ruta=ruta[i], nombre_cliente=nombre_cliente[i], nombre_calle_direccion=nombre_calle_direccion[i], colonia_barrio_distrito=colonia_barrio_distrito[i], departamento=departamento[i], referencia=referencia[i], dni_ruc=dni_ruc[i], contacto=contacto[i], telefono=telefono[i], horario_atencion=horario_atencion[i], modelo_ef=modelo_ef[i], logo=logo[i], tamaño=tamaño[i], activo=activo[i], status_validacion=status_validacion[i], fecha_validacion=fecha_validacion_str[i], motivo_rechazo=motivo_rechazo[i], explicacion_rechazo=explicacion_rechazo[i], bonificacion=bonificacion[i], proceso_ejecucion=proceso_ejecucion[i], fecha_ejecucion=fecha_ejecucion_str[i])
                    cloud.save()

                return render(request, self.template_name)
            except:
                return render(request, self.template_name)
        else:
            mensaje = 'La memoria esta llena'
            context = {'mensaje': mensaje}
            return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        pass
