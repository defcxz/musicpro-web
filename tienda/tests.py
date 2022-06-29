from django.test import TestCase
from products.templatetags.tag import convertir
from products.models import Product
import requests

# Create your tests here.

class ApiTestCase(TestCase):
    # Para poner en marcha el test, se crea la función setUp para crear el objeto de prueba con el que se va a trabajar
    def setUp(self):
        Product.objects.create(title='Producto de Prueba', price=10000)
        print("Método setUp: Producto de prueba creado.")

    # Se prueba la conexión a la API
    def test_api_conexion(self):
        try:
            convertir(Product.objects.get(title='Producto de Prueba').price)
            print("Método test_api_conexion: Conexión exitosa.")
        except:
            print("Método test_api_conexion: Conexión fallida.")
            self.fail("Método test_api_conexion: Conexión fallida.")

    # Se prueba que el precio credo convertido sea igual al precio que se obtiene de la API
    def test_conversion_precios(self):
        url = 'https://v6.exchangerate-api.com/v6/e066b266eec3a2e468d81caf/pair/CLP/USD/' + str(Product.objects.get(title='Producto de Prueba').price)

        res = requests.get(url)
        conv = convertir(Product.objects.get(title='Producto de Prueba').price)

        data = res.json()
        print("Resultado de la API: $" + str(round(data['conversion_result'],2)) + " \nResultado de la función: $" + str(conv))
        self.assertEqual(conv, str(round(data['conversion_result'],2)))

        