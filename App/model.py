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

import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import listiterator as it
from DISClib.DataStructures import liststructure as lt
from DISClib.DataStructures import mapentry as me



"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""
# ___________________________________________________
#  Implementacion 0
# ___________________________________________________

def initCatalog():
    """
    Llama la funcion de inicializacion del TAD list.
    """
    catalog = lt.newList(datastructure="ARRAY_LIST")
    return catalog
    
def loadCSVFile (lst , file):
    lst=lt.newList(datastructure="ARRAY_LIST")
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        with open( file, encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for elemento in row: 
                lt.addLast(lst,elemento)
    except:
        print("Hubo un error con la carga del archivo")
    return lst

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

def newCatalog():
    """
    Crea un nuevo catalogo.
    """
    Data={'casting': None, 'details': None}
    catalog={ 'Data': Data 'production_companies': None, 'director_name': None, 'actor_name': None 
    'genres':None, 'production_countries': None}

    catalog['Data']['casting']=lt.newList(datastructure='ARRAY_LIST')
    catalog['Data']['details']=lt.newList(datastructure='ARRAY_LIST')

    catalog['production_companies']=mp.newMap(numelements=(countBy('production_companies', catalog['Movies'])),
                                        maptype='CHAINING',
                                        loadfactor=0.4)
    catalog['director_name']=mp.newMap(numelements=countBy('director_name',catalog['Movies']), 
                                        maptype='PROBING', 
                                        loadfactor=0.4)
    catalog['actor_name']=mp.newMap(numelements=(countBy('actor_name',catalog['Movies'])), 
                                        maptype='PROBING', 
                                        loadfactor=0.4)
    catalog['genres']=mp.newMap(numelements=(countBy('genres', catalog['Movies'])), 
                                        maptype='PROBING', 
                                        loadfactor=0.4)
    catalog['production_countries']=mp.newMap(numelements=(countBy('production_countries', catalog['Movies'])), 
                                        maptype='PROBING', 
                                        loadfactor=0.4)


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
def NewComopanies(company_name):
    """
    Crea un nuevo elemento de las compañias 
    """
    company={'name': '', 'movies':None, 'vote_avg': None}
    company['name']=company_name
    company_name['movies']=lt.newList(datastructure='ARRAY_LIST')
    return company



def addMovie(catalog, movie, info)
    """
    Agregar una pelicula.
    """
    if info == '1':
        movies=catalog['Data']['casting']
        lt.addLast(movies, movie)
    elif info =='2':
        movies=catalog['Data']['details']
        lt.addLast(movies, movie)
    










def addCompanie(company_name, movie,catalog):
    """
    Agrega una nueva compañia al mapa de productoras
    """
    comapnies=catalog['production_companies']
    exist=mp.contains(comapnies, company_name)
    if exist:
        entry=mp.get(comapnies, company_name)
        company=me.getValue(entry)
    else:
        company=NewComopanies(company_name)
        mp.put(comapnies, company_name, company)
    lt.addLast(comapnies['movies'], movie)

    avg_cp=company['vote_avg']
    avg_mv=movie['vote_average']
    if avg_cp == None:
        company['vote_avg']=float(avg_mv)
    else:
        company['vote_avg']= round((company['vote_avg']+ float(avg_mv))/2,2)
    

                                         
# ___________________________________________________
#  Funciones generales implementadas
# ___________________________________________________
def getFirstLastMovies(catalog):
    """
    Retorna el primer y ultimo libro de la lista.
    """
    first_movie=lt.firstElement(catalog)
    last_movie=lt.lastElement(catalog)
    return (first_movie, last_movie)

def countBy(criteria, lst):
    """
    cuenta la cantidad de elementos por un crterio.
    """
    number=0
    names=[]
    for element in lst:
        if element[criteria] not in names:
            number=+1
            names.appende(element[criteria])
    return number