from django.contrib import admin
from .models import Categoria, Proyecto, TipoDoc, Documento

# Register your models here.
# Registro de modelo Categoria
class CategoriaModelo(admin.ModelAdmin):
    list_display=["lenguaje"]
    #list_display_links=["lenguaje"]
    class Meta:
        model:Categoria
admin.site.register(Categoria)

#Registro de modelo Proyecto
class ProyectoModelo(admin.ModelAdmin):
    list_display=["nombreProyecto"]
    class Meta:
        models=Proyecto
admin.site.register(Proyecto)

#Registro de modelo TipoDoc
class TipoDocumentoModelo(admin.ModelAdmin):
    list_display=["nombreTipoDoc"]
    class Meta:
        models=TipoDoc
admin.site.register(TipoDoc)

#Registro de modelo Documento
class DocumentoModelo(admin.ModelAdmin):
    list_display=["nombreDoc"]
    class Meta:
        models=Documento
admin.site.register(Documento)