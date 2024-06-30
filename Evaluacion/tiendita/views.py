from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistroForm
from .models import Usuario
from django.shortcuts import render, get_object_or_404
from .forms import UsuarioForm
from django.contrib.auth.decorators import login_required  # Asegura que el usuario esté autenticado
from .forms import CustomAuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # Importa el modelo de usuario de Django
from django.contrib.auth import authenticate, login as auth_login
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

def registrarse(request):
    context={}
    return render(request, 'tiendita/registrarse.html',context)

# views.py


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Asegúrate de que 'index' sea el nombre correcto de tu URL
        else:
            print(form.errors)  # Imprimir errores para depuración
    else:
        form = RegistroForm()
    
    return render(request, 'tiendita/registrarse.html', {'form': form})


def administracion(request):
    # Lógica para la vista de administración, si es necesaria
    return render(request, 'tiendita/administracion.html')

def administracion(request):
    # Obtener todos los usuarios registrados
    usuarios = Usuario.objects.all()

    # Pasar los usuarios a la plantilla para mostrarlos
    return render(request, 'tiendita/administracion.html', {'usuarios': usuarios})

def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('administracion')  # Redirige a la página de administración después de editar
    else:
        form = UsuarioForm(instance=usuario)
    
    return render(request, 'tiendita/editar_usuario.html', {'form': form, 'usuario': usuario})

def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    
    if request.method == 'POST':
        print(f"Eliminando usuario: {usuario.email}")  # Verificación en consola
        usuario.delete()
        print(f"Usuario eliminado correctamente.")  # Verificación en consola
        return redirect('administracion')  # Redirige de vuelta a la página de administración
    
    return render(request, 'tiendita/eliminar_usuario.html', {'usuario': usuario})

def index(request):
    return render(request, 'tiendita/index.html')
