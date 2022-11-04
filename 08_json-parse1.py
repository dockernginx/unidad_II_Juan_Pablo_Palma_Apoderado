'''
Nombre: Juan Pablo Palma APoderado 
Fecha: 25/oct/2022
Descricpción: Este ejercicio no centraremos en cosas muy basicas solo para mostrar como se ejecuta. 
'''
import urllib.parse
'''Importe módulos existentes para agregar funcionalidad adicional'''
import requests
'''main_api - la URL principal a la que está accediendo'''
main_api = "https://www.mapquestapi.com/directions/v2/route?"
'''orig - el parámetro para especificar su punto de origen'''
orig = "Washington"
'''dest - el parámetro para especificar su destino'''
dest = "Baltimaore"
'''key: la clave del consumidor de la API de MapQuest que recuperó del sitio web del desarrollador'''
key  = "your_api_key"
url  = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
'''Cree una variable que usando el método get para solicitar datos JSON de la URL enviada.'''
json_data = requests.get(url).json()
'''Imprima los resultados para verificar que la solicitud fue exitosa.'''
print(json_data)