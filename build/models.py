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

