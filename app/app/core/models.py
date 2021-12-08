from django.db import models


class Categoria(models.Model):
    name = models.CharField(verbose_name='Categoria', max_length=50, unique=True)
    description= models.TextField(verbose_name='Descripcion de la Categoria', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= 'Categoria'
        verbose_name_plural= 'Categorias'



# Create your models here.
class Articulo(models.Model):
    category= models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Seleccione la categoria')
    name = models.CharField(verbose_name='Articulo', max_length=100, unique=True)
    description = models.TextField(verbose_name='Descripción del Articulo', max_length=200)
    code = models.IntegerField(verbose_name='Codigo')
    avatar= models.ImageField(verbose_name='Agregar Imagen', null=True, upload_to='imgArticulos')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= 'Articulo'
        verbose_name_plural= 'Articulos'



class Cliente(models.Model):
    name= models.CharField(verbose_name='Nombre Completo', max_length=50, unique=True)
    address=models.CharField(verbose_name='Dirección', max_length=200)
    phone=models.IntegerField(verbose_name='Número de Teléfono')
    rfc=models.CharField(verbose_name='RFC', max_length=14)
    email=models.CharField(verbose_name='E-MAIL',max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= 'Cliente'
        verbose_name_plural= 'Clientes'



class Usuario(models.Model):
    name= models.CharField(verbose_name='Nombre Completo', max_length=50, unique=True)
    address=models.CharField(verbose_name='Dirección', max_length=200)
    phone=models.IntegerField(verbose_name='Número de Teléfono')
    curp=models.CharField(verbose_name='CURP', max_length=20)
    nss=models.CharField(verbose_name='Número de Seguro Social', max_length=10)
    rfc=models.CharField(verbose_name='RFC', max_length=14)
    email=models.CharField(verbose_name='E-MAIL',max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= 'Usuario'
        verbose_name_plural= 'Usuarios'



class Proveedor(models.Model):
    name= models.CharField(verbose_name='Nombre Completo', max_length=50, unique=True)
    address=models.CharField(verbose_name='Dirección', max_length=200)
    phone=models.IntegerField(verbose_name='Número de Teléfono')
    email=models.CharField(verbose_name='E-MAIL',max_length=50)
    numdocumento=models.IntegerField(verbose_name='Número de Documento')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= 'Proveedor'
        verbose_name_plural= 'Proveedores'



class Ingreso(models.Model):
    proveedor= models.CharField(verbose_name='Nombre Completo', max_length=50, unique=True)
    date=models.DateTimeField(verbose_name='Fecha')
    seriecomprobante=models.IntegerField(verbose_name='Serie de Comprobante')
    piezas=models.IntegerField(verbose_name='Total de Piezas')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= 'Ingreso'
        verbose_name_plural= 'Ingresos'


class Venta(models.Model):
    cliente= models.CharField(verbose_name='Nombre Completo', max_length=50, unique=True)
    date=models.DateTimeField(verbose_name='Fecha')
    seriecomprobante=models.IntegerField(verbose_name='Serie de Comprobante')
    total=models.FloatField(verbose_name='Total')
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= 'Venta'
        verbose_name_plural= 'Ventas'