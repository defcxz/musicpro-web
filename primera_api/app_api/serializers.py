# Serializers.py
# En este archivo vamos a definir que campos
# vamos a mostrar.

from django.contrib.auth.models import User, Group
from tienda.models import Producto
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = User
        fields = ['url', 'username', 'password' , 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = Group
        fields = ['url', 'name']

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = Producto
        fields = ['url', 'serie_producto', 'código' , 
                'nombre' , 'marca' , 'precio_actual' ]
        

