from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario

# Create your views here.
def index(request):
    context={}
    return render(request, 'tiendita/index.html',context)

def arbustos(request):
    context={}
    return render(request, 'tiendita/arbustos.html',context)

def flores(request):
    context={}
    return render(request, 'tiendita/flores.html',context)

def maceteros(request):
    context={}
    return render(request, 'tiendita/maceteros.html',context)

def tierradehojas(request):
    context={}
    return render(request, 'tiendita/tierradehojas.html',context)

def registrar_usuario(request):
    if request.method == 'POST':
        email = request.POST['email']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        telefono = request.POST['telefono']
        contrasena = request.POST['contrasena']

        usuario = Usuario.objects.create(
            email=email, nombre=nombre, apellido=apellido, telefono=telefono, contrasena=contrasena)
        messages.success(request, '¡Usuario registrado!')
        return redirect('/')
    return render(request, "registro_usuario.html")  # Supongo que tienes una plantilla llamada registro_usuario.html

def editar_usuario(request, pk):
    usuario = Usuario.objects.get(pk=pk)
    return render(request, "editar_usuario.html", {"usuario": usuario})

def actualizar_usuario(request):
    if request.method == 'POST':
        pk = request.POST['pk']
        email = request.POST['email']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        telefono = request.POST['telefono']
        contrasena = request.POST['contrasena']

        usuario = Usuario.objects.get(pk=pk)
        usuario.email = email
        usuario.nombre = nombre
        usuario.apellido = apellido
        usuario.telefono = telefono
        usuario.contrasena = contrasena
        usuario.save()

        messages.success(request, '¡Usuario actualizado!')
        return redirect('/')
    return redirect('/')

def eliminar_usuario(request, pk):
    usuario = Usuario.objects.get(pk=pk)
    usuario.delete()
    messages.success(request, '¡Usuario eliminado!')
    return redirect('/')
