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
    catalog={ 'Data': Data, 'production_companies': None, 'IDs':None,
    'director_name': None, 'actor_name': None,'genres':None, 'production_countries': None}

    catalog['Data']['casting']=lst1
    catalog['Data']['details']=lst2


    #catalog['IDs']=mp.newMap(numelements=(lt.size(catalog['Data']['details'])),
                                        #maptype='CHAINIG',
                                        #loadfactor=1,
                                        #comparefunction=ct.cmpfunctionID)
    catalog['production_companies']=mp.newMap(numelements=(countBy('production_companies',catalog['Data']['details'])),
                                        maptype='PROBING',
                                        loadfactor=0.4, 
                                        comparefunction=cmpfunctionCompanies)
    catalog['director_name']=mp.newMap(numelements=(countBy('director_name',catalog['Data']['casting'])), 
                                        maptype='PROBING', 
                                        loadfactor=0.4,
                                        comparefunction= cmpfunctionDirectors)
    catalog['actor_name']=mp.newMap(numelements=(countActors(catalog['Data']['casting'])), 
                                        maptype='PROBING', 
                                        loadfactor=0.4,
                                        comparefunction= cmpfunctionActor)
    catalog['genres']=mp.newMap(numelements=(countGenres(catalog['Data']['details'])), 
                                        maptype='PROBING', 
                                        loadfactor=0.4,
                                        comparefunction= cmpfunctionGenres)
    catalog['production_countries']=mp.newMap(numelements=(countBy('production_countries',catalog['Data']['details'])), 
                                        maptype='PROBING', 
                                        loadfactor=0.4,
                                        comparefunction= cmpfunctionCountry)
    return catalog 

def newComopanies(company_name):
    """
    Crea un nuevo elemento de las compañias. 
    """
    company={'name': None, 'movies':None, 'vote_avg': None}
    company['name']=company_name
    company['movies']=lt.newList(datastructure='SINGLE_LINKED', cmpfunction= cmpfunctionCompanies)
    return company

def newDirector(director_name):
    """
    Crea un nuevo elemento de los directores.
    """
    director={'name': None, 'movies': None, 'details': None, 'vote_avg': None}
    director['name']=director_name
    director['movies']=lt.newList(datastructure='SINGLE_LINKED')
    director['details']=lt.newList(datastructure='SINGLE_LINKED')
    return director

def newActor(actor_name):
    """
    Crea un nuevo elemento de los actores.
    """
    actor={'name': None, 'movies': None, 'details': None,'vote_avg': None}
    actor['name']=actor_name
    actor['movies']=lt.newList(datastructure='SINGLE_LINKED')
    actor['details'] = lt.newList(datastructure='SINGLE_LINKED')
    return actor 

def newGenre(genre_name):
    """
    Crea un nuevo elemento de generos.
    """
    genre={'name': None, 'movies': None, 'vote_count': None}
    genre['name']=genre_name
    genre['movies']=lt.newList(datastructure='SINGLE_LINKED')
    return genre

def newCountry(country_name):
    """
    Crea un nuevo elemento de paises.
    """
    country={'name':None, 'movies':None, 'vote_avg': None}
    country['name']=country_name
    country['movies']=lt.newList(datastructure='SINGLE_LINKED')
    return country

def newID(ID):
    """
    Crea un nuevo elemento de ID.
    """
    elemnt={'ID':None, 'details':None, 'casting':None, 'vote_avg':None}
    elemnt['ID']=ID
    return elemnt

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

def addCompany(movie,catalog):
    """
    Agrega una nueva compañia al mapa de productoras
    """
    companies=catalog['production_companies']
    company_name=movie['production_companies']
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

def addDirector(movie2, movie1, catalog):
    """
    Agrega informacion de un director en el mapa de directores.
    """
    directors=catalog['director_name']
    director_name=movie2['director_name']
    exist=mp.contains(directors, director_name)
    if exist:
        entry=mp.get(directors, director_name)
        director=me.getValue(entry)
    else:
        director=newDirector(director_name)
        mp.put(directors, director_name, director)
    lt.addLast(director['movies'], movie2)
    lt.addLast(director['details'], movie1)
    avg_dt=director['vote_avg']
    avg_mv=movie1['vote_average']
    if avg_dt == None:
        director['vote_avg']=float(avg_mv)
    else:
        director['vote_avg']= round(((avg_dt+ float(avg_mv))/2),2) 

def addActor(movie2, movie1, catalog):
    """
    Agrega informacion de un actor en el mapa de actores.
    """
    actors=catalog['actor_name']
    actor1=movie2['actor1_name']
    if actor1 != None:
        exist=mp.contains(actors, actor1)
        if exist:
            entry=mp.get(actors, actor1)
            actor=me.getValue(entry)
        else:
            actor=newActor(actor1)
            mp.put(actors, actor1, actor)
        lt.addLast(actor['movies'], movie2)
        lt.addLast(actor['details'], movie1)
        avg_at=actor['vote_avg']
        avg_mv=movie1['vote_average']
        if avg_at == None:
            actor['vote_avg']=float(avg_mv)
        else:
            actor['vote_avg']= round(((avg_at+ float(avg_mv))/2),2)

    actor2=movie2['actor2_name']
    if actor2 != None:
        exist=mp.contains(actors, actor2)
        if exist:
            entry=mp.get(actors, actor2)
            actor=me.getValue(entry)
        else:
            actor=newActor(actor2)
            mp.put(actors, actor2, actor)
        lt.addLast(actor['movies'], movie2)
        lt.addLast(actor['details'], movie1)
        avg_at=actor['vote_avg']
        avg_mv=movie1['vote_average']
        if avg_at == None:
            actor['vote_avg']=float(avg_mv)
        else:
            actor['vote_avg']= round(((avg_at+ float(avg_mv))/2),2)
    actor3=movie2['actor3_name']
    if actor3 != None:
        exist=mp.contains(actors, actor3)
        if exist:
            entry=mp.get(actors, actor3)
            actor=me.getValue(entry)
        else:
            actor=newActor(actor3)
            mp.put(actors, actor3, actor)
        lt.addLast(actor['movies'], movie2)
        lt.addLast(actor['details'], movie1)
        avg_at=actor['vote_avg']
        avg_mv=movie1['vote_average']
        if avg_at == None:
            actor['vote_avg']=float(avg_mv)
        else:
            actor['vote_avg']= round(((avg_at+ float(avg_mv))/2),2)
    actor4=movie2['actor4_name']
    if actor4 != None:
        exist=mp.contains(actors, actor4)
        if exist:
            entry=mp.get(actors, actor4)
            actor=me.getValue(entry)
        else:
            actor=newActor(actor4)
            mp.put(actors, actor4, actor)
        lt.addLast(actor['movies'], movie2)
        lt.addLast(actor['details'], movie1)
        avg_at=actor['vote_avg']
        avg_mv=movie1['vote_average']
        if avg_at == None:
            actor['vote_avg']=float(avg_mv)
        else:
            actor['vote_avg']= round(((avg_at+ float(avg_mv))/2),2)
    actor5=movie2['actor5_name']
    if actor5 != None:
        exist=mp.contains(actors, actor5)
        if exist:
            entry=mp.get(actors, actor5)
            actor=me.getValue(entry)
        else:
            actor=newActor(actor5)
            mp.put(actors, actor5, actor)
        lt.addLast(actor['movies'], movie2)
        lt.addLast(actor['details'], movie1)
        avg_at=actor['vote_avg']
        avg_mv=movie1['vote_average']
        if avg_at == None:
            actor['vote_avg']=float(avg_mv)
        else:
            actor['vote_avg']= round(((avg_at+ float(avg_mv))/2),2)

def addGenre(movie, catalog):
    """
    Agrega informacion de un genero en el mapa de generos.
    """
    genres=catalog['genres']
    genre_list=movie['genres'].split('|')
    for genre_name in genre_list:
        exist=mp.contains(genres, genre_name)
        if exist:
            entry=mp.get(genres, genre_name)
            genre=me.getValue(entry)
        else:
            genre=newGenre(genre_name)
            mp.put(genres, genre_name, genre)
        lt.addLast(genre['movies'], movie)
        count_gn=genre['vote_count']
        count_mv=movie['vote_count']
        if count_gn == None:
            genre['vote_count']=int(count_mv)
        else:
            genre['vote_count']=((count_gn+ int(count_mv))/2)

def addCountry(movie, catalog):
    """
    Agrega informacion de un país en el mapa de un país.
    """
    countries=catalog['production_countries']
    country_name=movie['production_countries']
    exist=mp.contains(countries, country_name)
    if exist:
        entry=mp.get(countries, country_name)
        country=me.getValue(entry)
    else:
        country=newCountry(country_name)
        mp.put(countries, country_name, country)
    lt.addLast(country['movies'], movie)

    avg_ct=country['vote_avg']
    avg_mv=movie['vote_average']
    if avg_ct == None:
        country['vote_avg']=float(avg_mv)
    else:
        country['vote_avg']=round(((avg_ct+ float(avg_mv))/2),2)

def addID(movie, catalog, info):
    """
    Agraga informacion al mapa ID deacuerdo a la info.
    """
    IDs=catalog['ID']
    ID=movie['id']
    exist=mp.contains(IDs, ID)
    if info==1:
        if exist:
            entry=mp.get(IDs, ID)
            ID_info=me.getValue(entry)
        else:
            ID_info=newID(ID)
            mp.put(IDs, ID, ID_info)
        lt.addLast(ID_info['casting'], movie)
    elif info ==2:
        if exist:
            entry=mp.get(IDs, ID)
            ID_info=me.getValue(entry)
        else:
            ID_info=newID(ID)
            mp.put(IDs, ID, ID_info)
        lt.addLast(ID_info['casting'], movie)
        avg_ID=ID_info['vote_avg']
        avg_mv=movie['vote_average']
        if avg_ID == None:
            ID_info['vote_avg']=float(avg_mv)
        else:
            ID_info['vote_avg']= round(((avg_ID+ float(avg_mv))/2),2)


#______________________________________________________
# Funciones de consulta
#______________________________________________________

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

def countGenres(lst):
    """
    cuenta la cantidad de elementos por un crterio.
    """
    number=0
    names=[]
    iterator=it.newIterator(lst)
    while it.hasNext(iterator):
        movie=it.next(iterator)
        genres_list=movie['genres'].split('|')
        for genre in genres_list:
            if genre not in names:
                number+=1
                names.append(genre)
    return number

def countActors(lst):
    """
    Cuenta los actores de la lista.
    """
    names=[]
    number=0
    iterator=it.newIterator(lst)
    while it.hasNext(iterator):
        movie=it.next(iterator)
        actor1=movie['actor1_name']
        actor2=movie['actor2_name']
        actor3=movie['actor3_name']
        actor4=movie['actor4_name']
        actor5=movie['actor5_name']
        if actor1 not in names:
            number+=1
            names.append(actor1)
        if actor2 not in names:
            number+=1
            names.append(actor2)
        if actor3 not in names:
            number+=1
            names.append(actor3)
        if actor4 not in names:
            number+=1
            names.append(actor4)
        if actor5 not in names:
            number+=1
            names.append(actor5)
    return number

def getElementCriteria(catalog, criteria, key):
    """
    Retorna el elemento a buscar de acuerdo al criterio
    """
    value= None
    if mp.contains(catalog[criteria], key):  
        entry=mp.get(catalog[criteria], key)
        value=me.getValue(entry)
    else:
        print('La llave no esta en el map')
    return value

def getCompany(catalog, company):
    """
    Busca la productora en el mapa de productoras del catalogo.
    """
    value= getElementCriteria(catalog, 'production_companies', company)
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

def getDirector(catalog, director):
    """
    Retorna a un director con su informacion.
    """
    value= getElementCriteria(catalog, 'director_name', director)
    try:
        movies=value['movies']
        info=value['details']
        lst=lt.newList(datastructure='SINGLE_LINKED')
        iterator=it.newIterator(info)
        while it.hasNext(iterator):
            movie=it.next(iterator)
            title=movie['title']
            lt.addLast(lst, title)
        avg=value['vote_avg']
        size=lt.size(movies)
        return (lst, size, avg)
    except:
        return None

def getActor(catalog, actor):
    """
    Retorna a un actor con su informacion.
    """
    value= getElementCriteria(catalog, 'actor_name', actor)
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
    Compara Compañias.
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
    Compara Directores.
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
    Compara Actores.
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
    Compara Generos.
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
    Compara Países.
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
    Compara IDs.
    """
    id = float(me.getKey(entry))
    element1= float(element1)
    if (element1 == id):
        return 0
    elif (element1 > id):
        return 1
    else:
        return -1