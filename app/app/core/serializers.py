from django.db import models
from  rest_framework import fields, serializers
from .models import Articulo, Categoria, Proveedor, Cliente, Usuario, Ingreso, Venta


class ArticuloSerializers(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = ['id', 'model', 'brand', 'description', 'image']

    def create(self, validated_data):
        return Articulo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.model = validated_data.get('model', instance.model)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.description = validated_data.get('description', instance.description)
        instance.imagen = validated_data.get('imagen', instance.imagen)
        instance.save()
        return instance

