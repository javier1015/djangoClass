from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from .genero import Generos
# Create your models here.
# estructurar la base de datos de la aplicacion userdata

# tabla rol.
class Roles(models.Model):
    roleName = models.CharField(max_length = 50)

    class Meta:
        verbose_name="Perfil de usuario"
        verbose_name_plural="Perfiles"

    def __str__(self):
        return self.roleName

# tabla datosUser
class DataUser(models.Model):
    idUser = models.CharField(max_length=20, verbose_name="Identificacion")
    nombreUser = models.CharField(max_length=255, null=True, verbose_name="Nombre")
    apellidoUser = models.CharField(max_length=255, null=True, verbose_name="Apellido")
    profesion = models.CharField(max_length=100, null=True, verbose_name="Profesion")
    fotoUser = models.ImageField(default = "user.png", upload_to="perfiles/img", verbose_name="Foto de perfil")
    telUser = models.CharField(max_length=20, verbose_name="Nunero de telefono")
    generoUser = models.CharField(max_length=20, choices=Generos, default="Otro")
    addData = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Creado el")
    update = models.DateTimeField(auto_now=True, null=True, verbose_name="Modificado el")

    class Meta:
        verbose_name="Datos de usuario"
        verbose_name_plural="Informacion"

    def __str__(self):
        return self.idUser

# tabla habilidades
class Habilidades(models.Model):
    nombreHabil = models.CharField(max_length=100)
    descripcionHabil = models.TextField(verbose_name="Descripcion habilidad")
        
    class Meta:
        verbose_name="Habilidades de usuario"
        verbose_name_plural="Competencias"
    
    def __str__(self):
        return self.nombreHabil

# tabla detaRol
class DetaRol(models.Model):
    idRol = models.ForeignKey(Roles, on_delete=models.CASCADE, verbose_name="identificador de erol")
    idUser = models.ForeignKey(DataUser, on_delete=models.CASCADE, verbose_name="identificador de usuario")
    addUser = models.DateTimeField(auto_now_add=True, auto_now=False)
    updateUser = models.DateTimeField(auto_now=True)
    estadoRol = models.CharField(max_length = 10)

    class Meta:
        verbose_name="Roles de usuario"
        verbose_name_plural="Roles"

    def __str__(self):
        return self.idUser

# tabla rate
class Rate(models.Model):
    idHabili = models.ForeignKey(Habilidades, on_delete=models.CASCADE, verbose_name="identificador de habilidades")
    idUser = models.ForeignKey(DataUser, on_delete=models.CASCADE, verbose_name="identificador de usuario")
    pocentajeHabil = models.DecimalField(max_digits=2, decimal_places=1)
    updateHabil = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Nivel de habilida"
        verbose_name_plural="Niveles de usuario"

    def __str__(self):
        return self.idUser
