from django.db import models

# Create your models here.

class DataFrameModel(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=200, blank=False, null=False, default=0)
    serie = models.CharField(max_length=200, blank=False, null=False, default=0)
    fuente = models.CharField(max_length=200, blank=False, null=False, default=0)
    pais = models.CharField(max_length=200, blank=False, null=False, default=0)
    cliente = models.CharField(max_length=200, blank=False, null=False, default=0)
    nombre = models.CharField(max_length=200, blank=False, null=False, default=0)
    direccion = models.CharField(max_length=200, blank=False, null=False, default=0)
    distrito = models.CharField(max_length=200, blank=False, null=False, default=0)
    activo = models.CharField(max_length=200, blank=False, null=False, default=0)
    tamaño = models.CharField(max_length=200, blank=False, null=False, default=0)
    imagen = models.CharField(max_length=200, blank=False, null=False, default=0)
    año = models.CharField(max_length=200, blank=False, null=False, default=0)
    fecha = models.CharField(max_length=200, blank=False, null=False, default=0)
    propiedad = models.CharField(max_length=200, blank=False, null=False, default=0)

    class Meta:
        verbose_name = 'DataFrameModel'
        verbose_name_plural = 'DataFrameModels'
        ordering = ['codigo']

    def __str__(self):
        return self.codigo


class BodegaModel(models.Model):
    id = models.AutoField(primary_key=True)
    csd_cvz = models.CharField(max_length=200, blank=False, null=False, default=0)
    cet = models.CharField(max_length=200, blank=False, null=False, default=0)
    nombre_cet = models.CharField(max_length=200, blank=False, null=False, default=0)
    frec = models.CharField(max_length=200, blank=False, null=False, default=0)
    ofvta = models.CharField(max_length=200, blank=False, null=False, default=0)
    oficina_ventas = models.CharField(max_length=200, blank=False, null=False, default=0)
    material = models.CharField(max_length=200, blank=False, null=False, default=0)
    codigo = models.CharField(max_length=200, blank=False, null=False, default=0)
    serie = models.CharField(max_length=200, blank=False, null=False, default=0)
    fuente = models.CharField(max_length=200, blank=False, null=False, default=0)
    pais = models.CharField(max_length=200, blank=False, null=False, default=0)
    ruta = models.CharField(max_length=200, blank=False, null=False, default=0)
    nombre = models.CharField(max_length=200, blank=False, null=False, default=0)
    direccion = models.CharField(max_length=200, blank=False, null=False, default=0)
    distrito = models.CharField(max_length=200, blank=False, null=False, default=0)
    distrito2 = models.CharField(max_length=200, blank=False, null=False, default=0)
    activo = models.CharField(max_length=200, blank=False, null=False, default=0)
    tamaño = models.CharField(max_length=200, blank=False, null=False, default=0)
    imagen = models.CharField(max_length=200, blank=False, null=False, default=0)
    año = models.CharField(max_length=200, blank=False, null=False, default=0)
    fecha_ingreso_taller = models.CharField(max_length=200, blank=False, null=False, default=0)
    propiedad = models.CharField(max_length=200, blank=False, null=False, default=0)

    class Meta:
        verbose_name = 'BodegaModel'
        verbose_name_plural = 'BodegaModels'
        ordering = ['codigo']

    def __str__(self):
        return self.codigo


class CloudModel(models.Model):
    id = models.AutoField(primary_key=True)
    serie = models.CharField(max_length=200, blank=False, null=False, default=0)
    proveedor = models.CharField(max_length=200, blank=False, null=False, default=0)
    plan = models.CharField(max_length=200, blank=False, null=False, default=0)
    dias = models.CharField(max_length=200, blank=False, null=False, default=0)
    prioridad = models.CharField(max_length=200, blank=False, null=False, default=0)
    movimientos = models.CharField(max_length=200, blank=False, null=False, default=0)
    tipo_servicio = models.CharField(max_length=200, blank=False, null=False, default=0)
    fecha_recepcion = models.CharField(max_length=200, blank=False, null=False, default=0)
    codigo_cliente = models.CharField(max_length=200, blank=False, null=False, default=0)
    sala_ventas = models.CharField(max_length=200, blank=False, null=False, default=0)
    columna1 = models.CharField(max_length=200, blank=False, null=False, default=0)
    mesa = models.CharField(max_length=200, blank=False, null=False, default=0)
    ruta = models.CharField(max_length=200, blank=False, null=False, default=0)
    nombre_cliente = models.CharField(max_length=200, blank=False, null=False, default=0)
    nombre_calle_direccion = models.CharField(max_length=200, blank=False, null=False, default=0)
    colonia_barrio_distrito = models.CharField(max_length=200, blank=False, null=False, default=0)
    departamento = models.CharField(max_length=200, blank=False, null=False, default=0)
    referencia = models.CharField(max_length=200, blank=False, null=False, default=0)
    dni_ruc = models.CharField(max_length=200, blank=False, null=False, default=0)
    contacto = models.CharField(max_length=200, blank=False, null=False, default=0)
    telefono = models.CharField(max_length=200, blank=False, null=False, default=0)
    horario_atencion = models.CharField(max_length=200, blank=False, null=False, default=0)
    modelo_ef = models.CharField(max_length=200, blank=False, null=False, default=0)
    logo = models.CharField(max_length=200, blank=False, null=False, default=0)
    tamaño = models.CharField(max_length=200, blank=False, null=False, default=0)
    activo = models.CharField(max_length=200, blank=False, null=False, default=0)
    status_validacion = models.CharField(max_length=200, blank=False, null=False, default=0)
    fecha_validacion = models.CharField(max_length=200, blank=False, null=False, default=0)
    motivo_rechazo = models.CharField(max_length=200, blank=False, null=False, default=0)
    explicacion_rechazo = models.CharField(max_length=200, blank=False, null=False, default=0)
    bonificacion = models.CharField(max_length=200, blank=False, null=False, default=0)
    proceso_ejecucion = models.CharField(max_length=200, blank=False, null=False, default=0)
    fecha_ejecucion = models.CharField(max_length=200, blank=False, null=False, default=0)
    class Meta:
        verbose_name = 'CloudModel'
        verbose_name_plural = 'CloudModels'
        ordering = ['id']

    def __str__(self):
        return self.id
