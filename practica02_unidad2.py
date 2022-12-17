"""
Descripción de la API: Esta API nos ayuda a encontrar la letra de una canción en especifico con solo introdcuir el 
nombre de la canción y el artista que la canta. 
Autor: Juan Pablo Palma Apoderado
Fecha de creación: 20 de noviembre 2022
"""
#DESCRIPCIÓN DE LA API
"""*******************************************************************************************************
Nombre de la API: Musixmatch
API Portal / Home Page: https://developer.musixmatch.com/
*******************************************************************************************************"""
import requests
import urllib.parse
main_api = " https://api.musixmatch.com/ws/1.1/matcher.lyrics.get?"
api_key  = "62a7e3ac94e3ac20aa3e6dd74c6b2156"
while True:
    print("Buscador de música")
    artist = input("artista o quit: ")
    if artist == "quit" or artist == "q":
        break
    track = input("canción o quit: ")
    if track == "quit" or track == "q":
        break
    url  = main_api + urllib.parse.urlencode({"q_track":track, "q_artist":artist,"apikey":api_key})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["message"]["header"]["status_code"]
    print(json_status)
    if json_status == 200:
        json_letra = json_data["message"]["body"]["lyrics"]["lyrics_body"]
        print("*************** Letra de la Canción: ", track ,"*****************", "\n",json_letra,"\n" )
    elif json_status == 404:
        print("**********************************************")
        print(str(json_data))
        print("Cancción o Artista no encontrado")
        print("**********************************************\n")
        print("=============================================")
    
