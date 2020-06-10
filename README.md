<a href="http://fvcproductions.com"><img src="https://raw.githubusercontent.com/Francisco-Huerta/Consorcio/master/image.png?token=AHETA76MMNDFYYTYLNRUMNC64DGE4" title="FVCproductions" alt="FVCproductions"></a>
# Consorcio
Este proyecto fue desarrollado usando Python 3.8.3, flask 1.1.2, connexion 2.7.0, fue utilizada la especificacion Swagger para validar la entrada y salida de información desde y hacia la API.

Esta configurado para correr en localhost:5000

La api para filtrar las farmacias de turno segun la comuna o el nombre está definida de la siguiente forma:
```
POST
https://localhost:5000/api/farmacias
Header
Content-Type: application/json
Parametro
json={'numeroComuna': numeroComuna, 'nombreFarmacia': nombreFarmacia}
```
el método que la define es filterer(nombre_numero) el cual será explicado más adelante

Se realizaron 6 unit tests que se encuentran en el archivo test.py:
1) Comprobar respuesta 200 
2) Comprobar que el tipo de contenido sea application/json
3) Validación de la información mínima requerida por las especificaciones
4) Comprobación de numero de comuna fuera de los límites (No existente)
5) Comprobación de un request con un nombre de farmacia inexistente
6) Comprobacion de la respuesta de un request vacío

# Archivos
farmacias.py
read_all(): Este es un método GET, responde a un request de api/farmacias, dando como respuesta un json string con las farmacias de turno

filterer(nombre_numero): Esta función POST filtra con dos parametros la lista de farmacias en turno, Nombre de Farmacia y Número de comuna, el nombre puede ser un substring, además no importa si el substring está en mayúsculas o minúsculas.
recibe un json string:

```python
nombreFarmacia = nombre_numero.get("nombreFarmacia", None)
numeroComuna = nombre_numero.get("numeroComuna", None)
```

devuelve un json string de las farmacias filtradas.

comunas.py
Este es el modulo de comunas y soporta todas las acciones ReST para
la colección de comunas

read(): Esta funcion responde a un request de api/comunas, retorna un string de la lista de comunas de la region metropolitana de la forma:

```html
<option value='0' selected>Elija Comuna</option><option value='82'>ALHUE...
```

home.js
Archivo que se encarga de recibir la información del backend, y usa esta para mostrarla en el frontend, además está encargada de enviar información al backend para filtrar según localidad y nombre de farmacia

home.html y home.css
Archivos encargados de mostrar, organizar y recibir información tanto del servidor como del usuario.


