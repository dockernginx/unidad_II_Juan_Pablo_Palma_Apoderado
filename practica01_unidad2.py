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
    json_status = json_data["ip"]
    print(json_status)
    #print(json_status) 
    if json_data == 0:
        print("IP:   " + str(json_data['ip']))
        print("code:   " + str(json_data['code']))
        print("name:   " + str(json_data['name']))
        print("symbol:   " + str(json_data['simbol']))
        print("=============================================\n")
    elif json_data == 402:
        print("**********************************************")
        print(str(json_data) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
        print("=============================================")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_data))
        print("************************************************************************\n")





