from blogapp.models import Cliente

from django.shortcuts import redirect, render
from .models import Cliente, Proveedor
from .forms import RegistroClienteForm, RegistroProveedorForm
# from .forms import RegistroClienteForm, LoginForm, UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.views.defaults import page_not_found
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def index(request):
    return render(request,"blogapp/index.html")

def usuarios(request):
    usuario=Cliente.objects.all()
    return render (request, 'blogapp/usuarios.html', {"data":usuario})

def ingreso(request):
    form = RegistroClienteForm()

    if request.method == 'POST':
        
        form = RegistroClienteForm(request.POST)

        if form.is_valid():

            cliente=Cliente()
            cliente.nombre=form.cleaned_data["nombre"]
            cliente.apellido=form.cleaned_data["apellido"]
            cliente.apellidoM=form.cleaned_data["apellidoM"]
            cliente.correo=form.cleaned_data["correo"]
            cliente.pais=form.cleaned_data["pais"]
            cliente.save()
            return redirect('ingreso')

        else:
            print('invalido')

    return render(request, 'blogapp/ingreso.html',{'form':form})

def ingresoproveedor(request):
    form = RegistroProveedorForm()

    if request.method == 'POST':
        
        form = RegistroProveedorForm(request.POST)

        if form.is_valid():

            proveedor=Proveedor()
            proveedor.razon_social=form.cleaned_data["razon_social"]
            proveedor.contacto=form.cleaned_data["contacto"]
            proveedor.correo=form.cleaned_data["correo"]
            proveedor.save()
            return redirect('proveedor')

        else:
            print('invalido')

    return render(request, 'blogapp/proveedor.html',{'formp':form})
    