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

def initCatalog(lst1,lst2):#no necesita revision
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    catalog = md.newCatalog(lst1, lst2)
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
    with open(file, encoding="utf-8") as movies:
        data_row=csv.DictReader(movies)
        for movie in data_row:
            md.addMovie(catalog, movie, info=1)

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
        md.addCompany(movie1, catalog)
        md.addGenre(movie1, catalog)
        md.addCountry(movie1, catalog)
    iterator=it.newIterator(catalog['Data']['details'])
    for movie2 in input_file2:
        movie1=it.next(iterator)
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
    value=md.getElementCriteria(catalog, 'production_companies', company)
    try:
        movies=value['movies']
        lst=lt.newList(datastructure='SINGLE_LINKED')
        iterator=it.newIterator(movies)
        while it.hasNext(iterator):
            movie=it.next(iterator)
            movie_name=movie['title']
            lt.addLast(lst, movie_name)
        avg=value['vote_avg']
        size=lt.size(movies)
        return (lst, avg, size)
    except:
        return None

def getActor(catalog, actor):
    """
    Retorna a un actor con su informacion.
    """
    value=md.getElementCriteria(catalog, 'actor_name', actor)
    try:
        movies=value['movies']
        info=value['details']
        lst=lt.newList(datastructure='SINGLE_LINKED')
        directors={}
        iterator1=it.newIterator(movies)
        iterator2=it.newIterator(info)
        while it.hasNext(iterator1):
            movie=it.next(iterator1)
            director=movie['director_name']
            if director in directors:
                directors[director]+=1
            else:
                director[director]=1
        while it.hasNext(iterator2):
            movie=it.next(iterator2)
            title=movie['title']
            lt.addLast(lst, title)
        avg=value['vote_avg']
        size=lt.size(movies)
        max_director=max(directors)
        return (lst, size, avg, max_director )
    except:
        return None
        
#______________________________________________________
# Funciones de Comparacion
#______________________________________________________

def cmpfunctionCompanies(element1, entry):
    """
    Compara dos compañias.
    """
    company = me.getKey(entry)
    if (element1 == company):
        return 0
    elif (element1 > company):
        return 1
    else:
        return -1

def cmpfunctionDirectors(element1, entry):
    """
    Compara dos compañias.
    """
    Director = me.getKey(entry)
    if (element1 == Director):
        return 0
    elif (element1 > Director):
        return 1
    else:
        return -1

def cmpfunctionActor(element1, entry):
    """
    Compara dos compañias.
    """
    Actor = me.getKey(entry)
    if (element1 == Actor):
        return 0
    elif (element1 > Actor):
        return 1
    else:
        return -1

def cmpfunctionGenres(element1, entry):
    """
    Compara dos compañias.
    """
    genre = me.getKey(entry)
    if (element1 == genre):
        return 0
    elif (element1 > genre):
        return 1
    else:
        return -1

def cmpfunctionCountry(element1, entry):
    """
    Compara dos compañias.
    """
    country = me.getKey(entry)
    if (element1 == country):
        return 0
    elif (element1 > country):
        return 1
    else:
        return -1

def cmpfunctionID(element1, entry):
    """
    Compara dos compañias.
    """
    id = int(me.getKey(entry))
    element1= int(element1)
    if (element1 == id):
        return 0
    elif (element1 > id):
        return 1
    else:
        return -1

# ___________________________________________________
#  Funciones generales implementadas
# ___________________________________________________


