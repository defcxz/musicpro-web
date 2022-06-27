# Serializers.py
# En este archivo vamos a definir que campos
# vamos a mostrar.

from products.models import Product
from rest_framework import serializers

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = Product
        fields = ['id', 
        'title', 
        'description' , 
        'price' ,
        'price' , 
        'created_at' ,
        'image' ]