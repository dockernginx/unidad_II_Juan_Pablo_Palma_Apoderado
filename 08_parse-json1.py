'''
Nombre: Juan Pablo Palma APoderado 
Fecha: 25/oct/2022
Descricpción: 
'''
import urllib.parse
from wsgiref.util import request_uri
main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington"
dest = "Baltimaore"
key  = "your_api_key"
url  = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
json_data = request_uri.get(url).json()
print(json_data)