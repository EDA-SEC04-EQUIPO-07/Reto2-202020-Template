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
import controller as ct
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------



# Funciones para agregar informacion al catalogo



# ==============================
# Funciones de consulta
# ==============================
def getFirtsLastBooks(catalog):
    """
    Retorna los primeros valores de la primera y ultima llave.
    """
    (firts,last)= ct.getFirstLastBooks(catalog)
    data_firts=[firts['title'], firts['release_date'],firts['vote_average'],firts['vote_count'],firts['original_language']]
    data_last=[last['title'], last['release_date'],last['vote_average'],last['vote_count'],last['original_language']]
    return (data_firts,data_last)


# ==============================
# Funciones de Comparacion
# ==============================


