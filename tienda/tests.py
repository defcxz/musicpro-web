from django.test import TestCase
from products.templatetags.tag import convertir
from products.models import Product
import requests

# Create your tests here.

class ApiTestCase(TestCase):
    # Para poner en marcha el test, se crea la función setUp para crear el objeto de prueba con el que se va a trabajar
    def setUp(self):
        print("Función setUp.")
        Product.objects.create(title='Producto de Prueba', price=10000)

    # Se prueba que el precio credo convertido sea igual al precio que se obtiene de la API
    def test_conversion_precios(self):
        print("Funcion de prueba de conversion de precios.")
        url1 = 'https://v6.exchangerate-api.com/v6/e066b266eec3a2e468d81caf/pair/CLP/USD/' + str(Product.objects.get(title='Producto de Prueba').price)

        res1 = requests.get(url1)
        c1 = convertir(Product.objects.get(title='Producto de Prueba').price)

        data = res1.json()
        self.assertEqual(c1, str(round(data['conversion_result'],1)))