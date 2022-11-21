"""
Descripción de la API: Es una Api que nos ayudara a saber los juegos siguientes del Real Madrid
dirección IP
Autor: Juan Pablo Palma Apoderado
Fecha de creación: 20 de noviembre 2022
"""
#DESCRIPCIÓN DE LA API
"""*******************************************************************************************************
Nombre de la API: Football-Data.Org
API Portal / Home Page:https://www.football-data.org/
*******************************************************************************************************"""
import requests
import urllib.parse

main_api = 'https://api.football-data.org/v4/teams/86/matches?'
headers = { 'X-Auth-Token': '57b06c76d67f4647a6db3430ec87f469'}

while True:
  print('Puede usar la palabra SCHEDULED')
  status = input("Ver los partidos de que equipo:")
  if status == "quit" or status == "q":
        break
  url = main_api + urllib.parse.urlencode({"status":status})
  print("URL: " + (url))
  json_data = requests.get(url, headers=headers).json()
  json_status = json_data["filters"]
  if json_data == 0:
        print("id:   " + str(json_data['id']))
        print("name:   " + str(json_data['name']))
        print("code:   " + str(json_data['code']))
        print("flag:   " + str(json_data['flag']))
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

#for match in response.json()['matches']:
#  print(match)