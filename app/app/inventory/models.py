from django.db import models

# Create your models here.
class Articulo(models.Model):
    nombre = models.CharField(verbose_name='Nombre del Articulo', max_length=100, unique=True)
    descripcion = models.TextField(verbose_name='Descripción del Articulo', max_length=200)
    codigo = models.IntegerField(verbose_name='Codigo')
    foto = models.ImageField(verbose_name='Agregar Imagen', null=True, upload_to='Inventario')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= 'Articulo a Inventariar'
        verbose_name_plural= 'Articulos a Inventariar'


class Inventario(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, verbose_name='Seleccione el producto')
    fechaIngreso = models.DateTimeField(verbose_name='Fecha y hora de ingreso')
    reacondicinado = models.BooleanField(verbose_name='¿Es reacondicionado?', default=False)

    def __str__(self):
        return 'Articulo {0}, se ingreso el {1}'.format(self.articulo, self.fechaIngreso)

    class Meta:
        verbose_name= 'Inventario'
        verbose_name_plural= 'Inventario'