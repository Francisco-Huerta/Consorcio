"""
Este es el modulo de comunas y soporta todas las acciones ReST para
la colección de comunas
"""

# 3rd party modules
import requests

def read():
    """
    Esta funcion responde a un request de api/comunas
    :return:        string de la lista de comunas de la region metropolitana de la forma: <option>
                    <option value='0' selected>Elija Comuna</option><option value='82'>ALHUE...
    """
    url = "https://midastest.minsal.cl/farmacias/maps/index.php/utilidades/maps_obtener_comunas_por_regiones"
    myobj = { 'reg_id': '7' }
    responses = requests.post(url, data = myobj)
    comunas = responses.text
    return comunas
