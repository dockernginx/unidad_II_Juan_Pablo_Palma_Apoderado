"""
Descripción de la API: Es una API que nos mostrar dos imagenes de un misma raza de gatos
dirección IP
Autor: Juan Pablo Palma Apoderado
Fecha de creación: 20 de noviembre 2022
"""
#DESCRIPCIÓN DE LA API
"""*******************************************************************************************************
Nombre de la API: The Cat Api
API Portal / Home Page: https://thecatapi.com/?ref=apilist.fun
*******************************************************************************************************"""
import requests
import urllib.parse
main_api = "https://api.thecatapi.com/v1/images/search?"
#https://api.thecatapi.com/v1/images/search?limit=10&breed_ids=beng&api_key=REPLACE_ME
limit = 2
api_key  = "live_inPxUjEVW9ylKXq5nbcrraDta6YRuWGr16HOyXC3bS7Wp4xv0dptKVjMmybMyAwn"
while True:
    print("Recomiendo que vaya al pagina oficial y al apartado de BREEDS para elguir la raza de gato")
    print("breed_ids=beng or quit")
    ids = input("breed_ids: ")
    if ids == "quit" or ids == "q":
        break
    url  = main_api + urllib.parse.urlencode({"limit":limit, "breed_ids":ids, "api_key":api_key})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["breeds"]
    #print(json_data) 
    if json_data == 0:
        print("id:   " + str(json_data['id']))
        print("url:   " + str(json_data['url']))
        print("width:   " + str(json_data['width']))
        print("height:   " + str(json_data['height']))
        #print(json_data)
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