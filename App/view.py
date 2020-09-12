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
import controller as cn
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

file_cast=config.file_dir+'\Data\Movies\MoviesCastingRaw-small.csv'
file_details=config.file_dir+'\Data\Movies\SmallMoviesDetailsCleaned.csv'



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
    print('2- Consultar la ultima y primera pelicula.')
    print('0- Salir')

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    lst1=cn.initCatalog()
    lst2=cn.initCatalog()
    if inputs[0]=='1':
        print('caragndo datos...')
        lst1=md.loadDatarow(lst1, file_cast)
        lst2=md.loadDataDetails(lst2, file_details)
        print('La longitud de los datos es:\"',arraylist.size(lst1) ,'\"')
        print('La longitud de los datos es:\"',arraylist.size(lst2) ,'\"') 
    elif inputs[0]== '2':
        (first,last)=md.getFirstLastMovies(lst2)
        print('La cantidad total de peliculas es:', arraylist.size(lst2))
        print('La primera pelicula es: ')
        for data in first:
            print(data)
        print('La ultima pelicula es: ')
        for data in last:
            print(data)
    else:
        sys.exit(0)
sys.exit(0)