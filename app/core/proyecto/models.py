from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from userdata.models import DataUser
# Create your models here.
# Estructura de datos de la aplicacion proyecto

# Tabla categoria
class Categoria(models.Model):
    lenguaje = models.CharField(max_length=100, verbose_name="Lenguaje")
    motorDB = models.CharField(max_length=100, verbose_name="MotorDB")
    arquitectura = models.CharField(max_length=100, verbose_name="Arquitectura de software")
    
    class Meta:
        verbose_name="Categoria proyecto"
        verbose_name_plural="Categoria"

    def __str__(self):
        return self.lenguaje

# Tabla Proyecto
class Proyecto(models.Model):
    idcategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Identificador de categoria")
    nombreProyecto = models.CharField(max_length=100, verbose_name="Nombre del proyecto")
    descripcionProyecto = models.TextField(verbose_name="Descripcion del proyecto")
    imagenProyecto = models.ImageField(default="proyecto.png", verbose_name='Imagen de proyecto')
    fechaInicio = models.DateTimeField(auto_now_add = False, verbose_name="Inicio del proyecto")
    fechaFinal = models.DateTimeField(auto_now_add=False, verbose_name="Fecha final")
    urlProyecto = models.CharField(max_length=255, verbose_name="Directorio")
    estadoProyecto = models.CharField(max_length=45, verbose_name="Estado")

    class Meta:
        verbose_name="Datos del proyecto"
        verbose_name_plural="Proyecto"

    def __str__(self):
        return self.nombreProyecto

# Tabla tipoDocumento
class TipoDoc(models.Model):
    nombreTipoDoc = models.CharField(max_length=100, verbose_name="Tipo de documento")

    class Meta:
        verbose_name="Tipos documento" 
        verbose_name_plural="Tipo de documento"

    def __str__(self):
        return self.nombreTipoDoc

# Tabla Documentos
class Documento(models.Model):
    idTipoDocu = models.ForeignKey(TipoDoc, on_delete=models.CASCADE, verbose_name="Identificador de tipoDocu")
    idProyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, verbose_name="Identificador de Proyecto")
    idUsuario = models.ForeignKey(DataUser, on_delete=models.CASCADE, verbose_name="Identificador de usuario")
    nombreDoc = models.CharField(max_length=255, verbose_name="Nombre del documento")
    patchDoc = models.CharField(max_length=200, verbose_name="Patch")

    class Meta:
        verbose_name="Documentos"
        verbose_name_plural="Documento"

    def __str__(self):
        return self.nombreDoc    
