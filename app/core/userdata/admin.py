from django.contrib import admin
# importar las clases de los modelos
from .models import Roles, DataUser, Habilidades, DetaRol, Rate

# Register your models here.
# Registro del mdelo de roles
class RolModelo(admin.ModelAdmin):
    list_display = ["roleName"]
    # list_display_links = ["roleName"]
    # list_filter = ["roleName"]
    class Meta:
        model= Roles    
admin.site.register(Roles)

# Registro del modelo de DataUser
class DataUserModelo(admin.ModelAdmin):
    list_display = ["nombreUser", "apellidoUser"]
    list_display_links = ["nombreUser"]
    list_filter = ["nombreUser"]
    class Meta:
        model = DataUser
admin.site.register(DataUser)

# Registro del modelo de Habilidades
class HabilidadesModelo(admin.ModelAdmin):
    list_display = ["nombreHabil"]
    class Meta:
        model = Habilidades
admin.site.register(Habilidades)

# Registro de modelo de DetaRol
class DetaRolModelo(admin.ModelAdmin):
    list_display = ["idUser"]
    class Meta:
        model = DetaRol
admin.site.register(DetaRol)

# Registro de modelo de Rate
class RateModelo(admin.ModelAdmin):
    list_display = ["idUser"]
    class Meta:
        model = Rate
admin.site.register(Rate)