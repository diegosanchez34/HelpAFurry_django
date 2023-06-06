from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request, 'home/index.html', context)

def contactanos(request):
    context={}
    return render(request,'home/contactanos.html',context)

def crearusuario(request):
    context={}
    return render(request,'home/crearusuario.html',context)

def gatos(request):
    context={}
    return render(request,'home/gatos.html',context)

def login(request):
    context={}
    return render(request,'home/login.html',context)

def nosotros(request):
    context={}
    return render(request,'home/nosotros.html',context)

def perros(request):
    context={}
    return render(request,'home/perros.html',context)

def singin(request):
    context={}
    return render(request,'home/singin.html',context)