from django.shortcuts import render

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