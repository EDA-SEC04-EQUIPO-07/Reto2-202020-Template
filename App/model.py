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

#______________________________________________________
# Imports
#______________________________________________________


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import listiterator as it
from DISClib.DataStructures import liststructure as lt
from DISClib.DataStructures import mapentry as me
import controller as ct
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""

#______________________________________________________
# Funcion 0
#______________________________________________________

def newlist():
    """
    Crea una lista vacia.
    """
    lst=lt.newList
    return lst

def loadCSVFile (file, lst):
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

#______________________________________________________
# API del TAD Catalogo de peliculas
#______________________________________________________

def newCatalog(lst1, lst2):
    """
    Crea un nuevo catalogo.
    """
    Data={'casting': None, 'details': None}
    catalog={ 'Data': Data, 'production_companies': None, 'director_name': None, 'actor_name': None,'genres':None, 'production_countries': None}

    catalog['Data']['casting']=lst1
    catalog['Data']['details']=lst2

    catalog['production_companies']=mp.newMap(numelements=(countBy('production_companies',catalog['Data']['details'])),
                                        maptype='PROBING',
                                        loadfactor=0.4, 
                                        comparefunction=ct.cmpfunctionCompanies)
    catalog['director_name']=mp.newMap(numelements=(countBy('director_name',catalog['Data']['casting'])), 
                                        maptype='PROBING', 
                                        loadfactor=0.4)
    #catalog['actor_name']=mp.newMap(numelements=(countBy('actor_name',catalog['Data']['casting'])), 
                                        #maptype='PROBING', 
                                        #loadfactor=0.4)#Necesita mejoras, acceder a los actores
    catalog['genres']=mp.newMap(numelements=(countBy('genres',catalog['Data']['details'])), 
                                        maptype='PROBING', 
                                        loadfactor=0.4)
    catalog['production_countries']=mp.newMap(numelements=(countBy('production_countries',catalog['Data']['details'])), 
                                        maptype='PROBING', 
                                        loadfactor=0.4)
    return catalog 

def newComopanies(company_name):
    """
    Crea un nuevo elemento de las compañias. 
    """
    company={'name': '', 'movies':None, 'vote_avg': None}
    company['name']=company_name
    company['movies']=lt.newList(datastructure='ARRAY_LIST')
    return company

def newDirector(director_name):
    """
    Crea un nuevo elemento de los directores.
    """
    director={'name':'', 'movies': None, 'vote_avg': None}
    director['name']=director_name
    director['movies']=lt.newList(datastructure='ARRAY_LIST')
    return director

def newActor(actor_name):
    """
    Crea un nuevo elemento de los actores.
    """
    actor={'name': '', 'movies': None, 'vote_avg': None}
    actor['name']=actor_name
    actor['movies']=lt.newList(datastructure='ARRAY_LIST')
    return actor 

def newGenre(genre_name):
    """
    Crea un nuevo elemento de generos.
    """
    genre={'name': '', 'movies': None, 'vote_avg': None}
    genre['name']=genre_name
    genre['movies']=lt.newList(datastructure='ARRAY_LIST')
    return genre

def newCountry(country_name):
    """
    Crea un nuevo elemento de paises.
    """
    country={'name':None, 'movies':None, 'vote_avg': None}
    country['name']=country_name
    country['movies']=lt.newList(datastructure='ARRAY_LIST')
    return country


#______________________________________________________
# Funciones para agregar informacion al catalogo
#______________________________________________________

def addMovie(catalog, movie, info):
    """
    Agregar una pelicula.
    """
    if info == 1:
        movies=catalog['Data']['casting']
        lt.addLast(movies, movie)
    elif info ==2:
        movies=catalog['Data']['details']
        lt.addLast(movies, movie)

def addCompany(company_name, movie,catalog):
    """
    Agrega una nueva compañia al mapa de productoras
    """
    companies=catalog['production_companies']
    exist=mp.contains(companies, company_name)
    if exist:
        entry=mp.get(companies, company_name)
        company=me.getValue(entry)
    else:
        company=newComopanies(company_name)
        mp.put(companies, company_name, company)
    lt.addLast(company['movies'], movie)
    avg_cp=company['vote_avg']
    avg_mv=movie['vote_average']
    if avg_cp == None:
        company['vote_avg']=float(avg_mv)
    else:
        company['vote_avg']= round(((avg_cp+ float(avg_mv))/2),2)    

def addDirector(director_name, movie,catalog):
    """
    Agrega informacion de un director en el mapa de directores.
    """
    directors=catalog['director_name']
    exist=mp.contains(directors, director_name)
    if exist:
        entry=mp.get(directors, director_name)
        director=me.getValue(entry)
    else:
        director=newComopanies(director_name)
        mp.put(directors, director_name, director)
    lt.addLast(director['movies'], movie)
    avg_dc=director['vote_avg']
    avg_mv=movie['vote_average']
    if avg_dc == None:
        director['vote_avg']=float(avg_mv)
    else:
        director['vote_avg']= round(((avg_dc+ float(avg_mv))/2),2)

def addActor(actor_name, movie, catalog):
    """
    Agrega informacion de un actor en el mapa de actores.
    """
    actors=catalog['director_name']
    exist=mp.contains(actors, actor_name)
    if exist:
        entry=mp.get(actors, actor_name)
        actor=me.getValue(entry)
    else:
        actor=newComopanies(actor_name)
        mp.put(actors, actor_name, actor)
    lt.addLast(actor['movies'], movie)
    avg_at=actor['vote_avg']
    avg_mv=movie['vote_average']
    if avg_at == None:
        actor['vote_avg']=float(avg_mv)
    else:
        actor['vote_avg']= round(((avg_at+ float(avg_mv))/2),2)

def addGenre(genre_name, movie, catalog):
    """
    Agrega informacion de un genero en el mapa de generos.
    """
    genres=catalog['genre']
    exist=mp.contains(genres, genre_name)
    if exist:
        entry=mp.get(genres, genre_name)
        genre=me.getValue(entry)
    else:
        genre=newComopanies(genre_name)
        mp.put(genres, genre_name, genre)
    lt.addLast(genre['movies'], movie)
    avg_gn=genre['vote_avg']
    avg_mv=movie['vote_average']
    if avg_gn == None:
        genre['vote_avg']=float(avg_mv)
    else:
        genre['vote_avg']= round(((avg_gn+ float(avg_mv))/2),2)

def addCountry(country_name, movie, catalog):
    """
    Agrega informacion de un país en el mapa de un país.
    """
    countries=catalog['production_countries']
    exist=mp.contains(countries, country_name)
    if exist:
        entry=mp.get(countries, country_name)
        country=me.getValue(entry)
    else:
        country=newComopanies(country_name)
        mp.put(countries, country_name, country)
    lt.addLast(country['movies'], movie)

    avg_ct=country['vote_avg']
    avg_mv=movie['vote_average']
    if avg_ct == None:
        country['vote_avg']=float(avg_mv)
    else:
        country['vote_avg']= round(((avg_ct+ float(avg_mv))/2),2)


#______________________________________________________
# Funciones de consulta
#______________________________________________________

#def getElementCriterias(criteria, lts):
    """
    Busca los elementos de una lista de acuerdo a un criterio.
    """
    iterator=it.newIterator(lst)
    while it.hasNext(iterator):
        movie=it.next(iterator)

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
    iterator=it.newIterator(lst)
    while it.hasNext(iterator):
        movie=it.next(iterator)
        value=movie[criteria]
        if value not in names:
            number+=1
            names.append(value)
    return number