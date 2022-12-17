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
main_api = "https://api.ipgeolocation.io/timezone?"
#https://api.ipgeolocation.io/ipgeo?apiKey=API_KEY&ip=1.1.1.1&fields=time_zone
fields= "time_zone"
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
    json_status = json_data["geo"]
    json_country  = json_data["geo"]["country_name"]
    json_city  = json_data["geo"]["city"]
    json_ip  = json_data["geo"]["ip"]
    json_lati  = json_data["geo"]["latitude"]
    json_long  = json_data["geo"]["longitude"]
    json_zone = json_data["timezone"]
    json_year = json_data["year"]
    json_month = json_data["month"]
    print("*************************************************************")
    print("IP: " , json_ip)
    print("Pais: " , json_country)
    print("Ciudad: " , json_city)
    print("Latitud: " , json_lati)
    print("Longitud: " , json_long)
    print("Zona Horaria: " , json_zone)
    print("Año: " , json_year)
    print("Mes: " , json_month)
    print("*************************************************************")
    #print(json_status) 

