from django import template
import requests

register = template.Library()

@register.filter()
def convertir(precio):
   url = 'https://v6.exchangerate-api.com/v6/e066b266eec3a2e468d81caf/pair/CLP/USD/' + str(precio)

   res = requests.get(url)
   data = res.json()

   return(str(data['conversion_result']))