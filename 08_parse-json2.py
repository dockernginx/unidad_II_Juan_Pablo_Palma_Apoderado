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
print("URL: " + (url))

json_data = request_uri.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")
