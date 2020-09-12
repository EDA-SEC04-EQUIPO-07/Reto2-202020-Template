"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
import model as md
assert config
import csv

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

#______________________________________________________
# Inicializacion del Catalogo
#______________________________________________________

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    catalog = md.newCatalog()
    return catalog

# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________


def loadDataCast(catalog, file):
    """
    Carga los datos de las peliculas en el mapa
    """
    file_Cast= config.file_dir + file
    with open(file_Cast, encoding="utf-8") as movies:
        data_row=csv.DictReader(movies)
        for movie in data_row:
            md.addMovie(catalog, movie, info=1)

def loadDataDetails(catalog, file):
    """
    Carga los datos de las peliculas en el mapa
    """    
    file_Cast= config.file_dir + file
    with open(file_Cast, encoding="utf-8") as movies:
        data_row=csv.DictReader(movies)
        for movie in data_row:
            md.addMovie(catalog, movie, info=2)
#______________________________________________________
# Funciones de consulta
#______________________________________________________


#______________________________________________________
# Funciones de Comparacion
#______________________________________________________


# ___________________________________________________
#  Funciones generales implementadas
# ___________________________________________________


