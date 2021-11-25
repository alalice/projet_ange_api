#les imports :
import os
import http.client
from pip._vendor import requests
#les definitions :

def nv_dossier (nom_dsr):
    os.mkdir(nom_dsr)


def get_id(dicos):
  dicos.split()
  liste_ids = [] 
  for i in dicos :
    liste_ids.append(i)
  return liste_ids

def liste_id ():
  url = "https://apidofa.fff.fr/api/leagues"
  payload={}
  headers = {
    'Authorization': 'Bearer MjYwMTMzZjY5MTdjOWM2NzEzNzA4NDlhNmQ5OWM3ZDVhOGMwZjEzZjllMmYyMDVmZjE2YjQ0ODkzZjk3NTBjNQ'
  }
  response = requests.request("GET", url, headers=headers, data=payload)
  liste_dicos_leagues = response.text
  return liste_dicos_leagues


#les test :

#nv_dossier("momo")
#crée un dossier du nom de momo dans projet ange .

print(get_id(liste_id()))