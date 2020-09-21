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

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import arraylist
from DISClib.DataStructures import listiterator as it
import controller as ct
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________

file_cast='\Data\Movies\MoviesCastingRaw-small.csv'
file_details='\Data\Movies\SmallMoviesDetailsCleaned.csv'

# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________



# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    print('Bienvenido')
    print('1- Cargar datos.')
    print('2- Descubrir Productoras de cine.')
    print('0- Salir')


def menu():
    """
    Inicia el menu del programa.
    """
    lst1=ct.initlist()
    lst2=ct.initlist()
    catalog=None
    while True:
        printMenu()
        inputs = input('Seleccione una opción para continuar\n')
        if inputs =='1':
            print('caragndo datos...')
            lst1=ct.loadlist(file_cast, lst1)
            lst2=ct.loadlist(file_details, lst2)
            catalog=ct.initCatalog(lst1, lst2)
            ct.addElementsmapsDetails(catalog, file_details, file_cast)
            print('La longitud de los datos es:\"',arraylist.size(catalog['Data']['details']) ,'\"')
            print('La longitud de los datos es:\"',arraylist.size(catalog['Data']['casting']) ,'\"')
        elif inputs =='2':
            company=input('Ingrese el nombre de la productora de cine:\n')
            (movies, avg, size)=ct.getCompany(catalog, company)
            print('La compañia \"', company,'\" tiene un total de peliculas: ', str(size))
            print('Las peliculas son: ')
            for movie in movies:
                print(movie)
            print('Sus peliculas tienen un voto promedio de: \"', str(avg), '\"')
        elif inputs == '0':
            sys.exit(0)
        else:
            print('La opcion: \"', inputs,'\" no es correcta.\n')
    sys.exit(0)

menu()