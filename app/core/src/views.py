from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponse, redirect
from .forms import contactForm
from django.urls import reverse
from django.core.mail import EmailMessage

# Create your views here.

# Class index
class HomePageView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'titulo':'SOEL S.A.S', 'descripcion':'Software de gestión de inventario, administración del personal y manego pago de nomina.'})

# Class nosotros
class NosotrosPageView(TemplateView):
    template_name = "nosotros.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'titulo':'Equipo de desarrollo',
        'nombreB':'Brayan holguin Bedoya',
        'profesionB':'Desarrollador',
        'descripcionB':'Me consideró una persona muy curiosa siempre en búsqueda de nuevos conocimientos, apasionado por la naturaleza y la fotografía.',
        
        'nombreJ':'Javier Alonso Osorio Caro',
        'profesionJ':'Desarrollador'
        })

# Class informacion
class InfoPageView(TemplateView):
    template_name = "informacion.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'movimientos':'MOVIMIENTOS',
        'usuarios':'USUARIOS',
        'pagos':'PAGOS',
        
        'menuP':'Menu principal',
        'descripcion_menuP':'Este está compuesto con tres sub menús administrador, nómina y ajustes. El administrador está compuesto por: TRABAJOS, MOVIMIENTOS, INVENTARIO, CATEGORIAS, PRODUCTOS, ACTIVIDADES, PERSONAL, HISTORIAL. El menú de nómina está compuesto por: CARGA DE TRABAJOS y PAGOS. Y el menú de ajustes lo conforman CUENTA Y DATOS PERSONALES.',
        
        'registroM':'Registro de movimientos',
        'descripcion_registriM':'Se elije el tipo de movimiento que se va realizar, se ingresa el código del producto y la cantidad de este .',
        'visualizarM':'Visualizacion de movimientos',
        'descripcion_visualizaM':'En esta se muestra el número del movimiento, el tipo al cual corresponde, la fecha en la cual fue realizado, y una opción de más detalles .',
        
        'registroPT':'Registro de productos',
        'descripcion_registroPT':'Se ingresa el código del producto, el nombre de este y se elige a que categoría pertenece.',
        'listaPT':'Lista de productos',
        'descripcion_listaPT':'En esta se puede apreciar el código del producto, el nombre la categoría y dos opciones editar y eliminar.'})

def contacto(request):
    formContact = contactForm()

    #validar que el formulario tenga una peticion post
    if request.method == "POST":
        formContact = contactForm(data=request.POST)
        if formContact.is_valid():
            tipoMensaje = request.POST.get('tipoMensaje', '')
            usuario = request.POST.get('usuario', '')
            correo = request.POST.get('correo', '')
            mensaje = request.POST.get('mensaje', '')

            # creamos el objeto con las variables del formulario
            email = EmailMessage(
                "RepoDevelopers, tienes un nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(usuario, correo, mensaje),
                "no-contestar@inbox.mailtrap.io",
                ["jo5334508@gmail.com"],
                reply_to =[correo]
            )
            # Enviams el correo:
            try:
                email.send()
                # Se envio el correo
                return redirect(reverse('contacto')+"?ok")
            except:
                # No se ha enviado el correo:
                return redirect(reverse('contacto')+"?fail")

    return render(request, 'contact.html', {'formulario':formContact})
