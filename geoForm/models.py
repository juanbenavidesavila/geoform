from django.db import models

from django.db import models


class Informe(models.Model):
  tipoIngreso = [
                    ["Fuente de Agua", "Fuente de Agua"],
                    ["Centro poblado, caserío, zona de vivienda", 
                     "Centro poblado, caserío, zona de vivienda"],
                    ["Centro educativo", "Centro educativo"],
                    ["Hospital o Centro de Salud", "Hospital o Centro de Salud"],
                    ["Zona conflicto armado", "Zona conflicto armado"],
                    ["Intituciones gubernamentales o Fundaciones", 
                     "Intituciones gubernamentales o Fundaciones"],
                    ["Empresas o Industrias", "Empresas o Industrias"],
                    ["Lugar que representa riesgo para la salud", 
                     "Lugar que representa riesgo para la salud"],
                    ["Zona de derrumbes o Deslizamientos", 
                     "Zona de derrumbes o Deslizamientos"],
                    ["Zonas de contaminación", "Zonas de contaminación"],
                    ["Parques o Reservas forestales", "Parques o Reservas forestales"],
                    ["Inindaciones", "Inindaciones"],
                    ["Comunidades indigenes", "Comunidades indigenes"],
                    ["Comunidades negras, afros, raizales o palenqueras", 
                     "Comunidades negras, afros, raizales o palenqueras"],
    
                   ]
  tipo_Ingreso = models.CharField(max_length=200, 
                                choices=tipoIngreso, 
                                default="Fuente de Agua")


  Direccion = models.CharField(max_length=100,
                              defaul="Región/calle/número")

  latitud = models.DecimalField(max_digits=50,
                                decimal_places=50,
                                blank=False,
                                null=False,
                                default="4.6482784")

  longitud = models.DecimalField(max_digits=5,
                                decimal_places=50,
                                blank=False,
                                null=False,
                                default="74.2726226")

  #auto_now_add Se anade una sola vez, cuando se crea el registro
  creacion = models.DateTimeField(auto_now_add=True)
  #auto_now Se modifica con cada cambio que se realize en el registro
  modificacion = models.DateTimeField(auto_now=True)

  class Meta:
      permissions = [("consultar_documentos", "Consultar documentos")]

      permissions = [("agregar_documento", "Agregar documento")]

      permissions = [("eliminar_documento", "Eliminar documento")]

# Create your models here.
