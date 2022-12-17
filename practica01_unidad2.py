"""
Descripción de la API: Esta API nos ayuda a encontrar todos los datos relacionados geologicamente solo nuestra 
dirección IP
Autor: Juan Pablo Palma Apoderado
Fecha de creación: 20 de noviembre 2022
"""
#DESCRIPCIÓN DE LA API
"""*******************************************************************************************************
Nombre de la API: Ip Geolocation Api
API Portal / Home Page:https://ipgeolocation.io/?ref=apilist.fun
*******************************************************************************************************"""
import requests
import urllib.parse
main_api = "https://api.ipgeolocation.io/ipgeo?"
#https://api.ipgeolocation.io/ipgeo?apiKey=API_KEY&ip=1.1.1.1&fields=time_zone
fields= "currency"
api_key  = "41210a321d7f4e6384b8af0a1bdcda9c"
excludes= "continent_code,currency,time_zone"
while True:
    print("Recomiendo que sepas tu dirección IP publica")
    ip = input("IP o quit: ")
    if ip == "quit" or ip == "q":
        break
    url  = main_api + urllib.parse.urlencode({"apiKey":api_key, "ip":ip, "fields":fields})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["currency"]
    json_code  = json_data["currency"]["code"]
    json_sim  = json_data["currency"]["name"]
    json_name  = json_data["currency"]["symbol"]
    print("*************************************************************")
    print("Codijo: " , json_code)
    print("Nombre: " , json_name)
    print("Simbolo: " , json_sim)
    print("*************************************************************")
    #print(json_status) 




