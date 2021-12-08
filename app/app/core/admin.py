from django.contrib import admin
from .models import*

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Articulo)
admin.site.register(Cliente)
admin.site.register(Usuario)
admin.site.register(Proveedor)
admin.site.register(Ingreso)
admin.site.register(Venta)