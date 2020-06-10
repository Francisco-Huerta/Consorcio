# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort
import requests

def read_all():
    """
    Esta funcion responde a un request de api/farmacias
    :return:        json string de la lista de farmacias de turno
    """
    # Create the list of drugstores from our data
    responses = requests.get("https://farmanet.minsal.cl/maps/index.php/ws/getLocalesRegion?id_region=7")
    farmacias = responses.json()
    return farmacias


def filterer(nombre_numero):
    """
    Esta función filtra con dos parametros, Nombre de Farmacia y Número de comuna, el nombre puede ser un substring,
    además no importa si está en mayúsculas o minúsculas
    :param numero_nombre:  Número de comuna y/o Nombre de farmacia para filtrar
    :return:        json string de Farmacias filtradas
    """
    nombreFarmacia = nombre_numero.get("nombreFarmacia", None)
    numeroComuna = nombre_numero.get("numeroComuna", None)

    
    responses = requests.get("https://farmanet.minsal.cl/maps/index.php/ws/getLocalesRegion?id_region=7")
    farmacias = responses.json()
    if numeroComuna and not numeroComuna == '0':
        farmacias = [x for x in farmacias if x['fk_comuna'] == numeroComuna]
    if nombreFarmacia:
        farmacias = [x for x in farmacias if nombreFarmacia.lower() in x['local_nombre'].lower() ]
    
    return farmacias
