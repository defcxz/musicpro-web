from django import template
import requests

register = template.Library()

@register.simple_tag()
def convertir(precio):
   url = 'https://v6.exchangerate-api.com/v6/e066b266eec3a2e468d81caf/pair/USD/CLP/' + str(precio)

   res = requests.get(url)
   data = res.json()

   return str(round(data['conversion_result']))