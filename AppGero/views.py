from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppGero.forms import UsuarioForm, ArticuloForm, HerramientaForm
from AppGero.models import Usuario, Articulo, Herramienta
from .forms import BuscarUsuarioFormulario

def inicio(request):
    return render(request, 'appgero/index.html')

def usuario(request):
    return render(request, 'appgero/usuario.html')

def articulo(request):
    return render(request, 'appgero/articulo.html')

def herramienta(request):
    return render(request, 'appgero/herramienta.html')


def agregar_usuario(request):
    if request.method == "POST":  # Si se envió el formulario
        usuario = Usuario(nombre=request.POST['nombre'],
        correo=request.POST['correo'],
        contrasenia=request.POST['contrasenia'],
        rol=request.POST['rol'])

        usuario.save()  # Guarda el usuario en la base de datos

        return redirect('inicio')  # Redirige a la página de inicio o a otra vista específica

    return render(request, "appgero/agregar_usuario.html")



def agregar_articulo(request):
    if request.method == "POST":  # Si se envió el formulario
        print("entra1")
        articulo = Articulo(titulo=request.POST["titulo"],
        contenido=request.POST["contenido"],
        autor=request.POST["autor"])
        print ("entra2")  # Crea un objeto Articulo

        articulo.save()  # Guarda el artículo en la base de datos
        
        return redirect('inicio')  # Redirige a la página de inicio o a otra vista específica
    
    return render(request, "appgero/agregar_articulo.html")


def agregar_herramienta(request):
    if request.method == "POST":
        herramienta = Herramienta(nombre=request.POST ["nombre"],
        descripcion=request.POST["descripcion"],
        url=request.POST["url"])

        herramienta.save()

        return redirect('inicio')

    return render(request, 'appgero/agregar_herramienta.html')

def buscar_usuario(request):
    resultados = None
    if request.method == "GET" and 'criterio' in request.GET:
        formulario = BuscarUsuarioFormulario(request.GET)
        if formulario.is_valid():
            termino = formulario.cleaned_data['criterio']
            resultados = Usuario.objects.filter(nombre__icontains=termino) | Usuario.objects.filter(correo__icontains=termino)
    else:
        formulario = BuscarUsuarioFormulario()

    return render(request, 'appgero/buscar_usuario.html', {'formulario': formulario, 'resultados': resultados})

def leerUsuarios (request):

    usuario = Usuario.objects.all()

    contexto = {"usuarios":usuario}

    return render (request, "appgero/leerUsuarios.html", contexto)

def leerArticulos (request):

    articulo = Articulo.objects.all()

    contexto = {"articulo":articulo}

    return render (request, "appgero/leerArticulos.html", contexto)

def leerHerramientas (request):

    herramienta = Herramienta.objects.all()

    contexto = {"herramientas":herramienta}

    return render (request, "appgero/leerHerramientas.html", contexto)