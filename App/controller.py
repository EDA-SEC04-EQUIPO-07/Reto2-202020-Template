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
from DISClib.DataStructures import listiterator as it
import model as md
assert config
import csv

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""


#______________________________________________________
# Funcion 0
#______________________________________________________

def initlist():
    """
    Crea una lista nueva.
    """
    lst=md.newlist()
    return lst

def loadlist(file, lst):
    """
    Carga elementos en una lista.
    """
    file= config.file_dir + file
    lst=md.loadCSVFile(file, lst)
    return lst

#______________________________________________________
# Inicializacion del Catalogo
#______________________________________________________

def initCatalog():#no necesita revision
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

#por terminar

def loadDataCast(catalog, file):
    """
    Carga los datos de las peliculas en el mapa.
    """
    file= config.file_dir + file
    dialect = csv.excel()
    dialect.delimiter=";"
    input_file=csv.DictReader(open(file, encoding="utf-8"), dialect=dialect)
    for movie in input_file:
        md.addMovie(catalog, movie, info=2)


def loadDataDetails(catalog, file):
    """
    Carga los datos de las peliculas en el mapa.
    """    
    file= config.file_dir + file
    dialect = csv.excel()
    dialect.delimiter=";"
    input_file=csv.DictReader(open(file, encoding="utf-8"), dialect=dialect)
    for movie in input_file:
        md.addMovie(catalog, movie, info=2)

def addElementsmapsDetails(catalog, file1, file2):
    """
    Carga los elementos de los mapas relacionados con los details.
    """
    file1= config.file_dir + file1
    dialect = csv.excel()
    dialect.delimiter=";"
    input_file1=csv.DictReader(open(file1, encoding="utf-8"), dialect=dialect)
    file2= config.file_dir + file2
    dialect = csv.excel()
    dialect.delimiter=";"
    input_file2=csv.DictReader(open(file2, encoding="utf-8"), dialect=dialect)
    for movie1 in input_file1:
        lt.addLast(catalog['Data']['details'], movie1)
        md.addCompany(movie1, catalog)
        md.addGenre(movie1, catalog)
        md.addCountry(movie1, catalog)
    iterator=it.newIterator(catalog['Data']['details'])
    for movie2 in input_file2:
        movie1=it.next(iterator)
        lt.addLast(catalog['Data']['casting'], movie2)
        md.addDirector(movie2, movie1, catalog)
        md.addActor(movie2, movie1, catalog)

#______________________________________________________
# Funciones de consulta
#______________________________________________________

def sizeList(lst):
    """
    Retorna la longitud de una lista.
    """
    return lt.size(lst)

def getCompany(catalog, company):
    """
    Busca la productora en el mapa de productoras del catalogo.
    """
    return md.getCompany(catalog, company)

def getDirector(catalog, director):
    """
    Retorna a un actor con su informacion.
    """
    return md.getDirector(catalog, director)

def getActor(catalog, actor):
    """
    Retorna a un actor con su informacion.
    """
    return md.getActor(catalog, actor)

def getGenre(catalog, genre):
    """
    Retorna un genero con su informacion.
    """
    return md.getGenre(catalog, genre)
def getCountry(catalog, country):
    """
    Retorna un genero con su informacion.
    """
    return md.getCountry(catalog, country)


