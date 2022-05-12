from django.contrib import admin
from .models import Cliente, Proveedor
from . import models

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Proveedor)
