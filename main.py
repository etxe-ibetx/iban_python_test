# -*- coding: utf-8 -*-

import csv
import sys

"""
Created on Sat Nov 21 15:38:40 2020

@author: Nerea
"""

TEST = True

lista_pilotos = []
lista_carreras = []
lista_resultados = []
lista_posiciones = []

# Constantes (Dato que no cambia)
PILOTOS_NOMBRE_ARCHIVO = "fichero_pilotos.csv"
CARRERAS_NOMBRE_ARCHIVO = "fichero_carreras.csv"
POSICIONES_NOMBRE_ARCHIVO = "fichero_posiciones.csv"

#FUNCIONES ESPECIALES
def mostrar_bienvenida():
    print ("******************")
    print ("╭━━━╮╱╭╮")
    print ("┃╭━━╯╭╯┃")
    print ("┃╰━━╮╰╮┃")
    print ("┃╭━━╯╱┃┃")
    print ("┃┃╱╱╱╭╯╰")
    print ("╰╯╱╱╱╰━━╯ \n")
    print ("******************")
    print ("Hola ", nombre_usuario, " !!")
    print ("Bienvenido al programa CLASSIFICATOR de FORMULA 1 \n")
    print ("Si pestañeas te lo pierdes! \n")

#FUNCIONES NIVEL 1 (GENERALES)
def mostrar_menuprin():   
    #nos devuelve un valor para opción
    opciones = ("1", "2", "3", "0")

    print ("--------------------------------------")
    print ("      ***   MENU PRINCIPAL    ***     ")
    print ("-------------------------------------- \n")
    print (" (1) Pilotos ")
    print (" (2) Carreras")
    print (" (3) Resultados y Clasificaciones  \n")
    print (" (0) Salir \n")

    opcion = input ("seleccione una opción: ")

    while opcion not in opciones:
        print ("Upps", nombre_usuario, ". No existe esa opción!!")
        opcion = input ("seleccione otra opcion: ")

    if opcion == "1":
        menu_pilotos()
    elif opcion == "2":
        menu_carreras()   
    elif opcion == "3":
        menu_resultados()     
    elif opcion== "0":    
        salir()

#FUNCIONES NIVEL 2 (GENERALES)   
def menu_pilotos():
    while(True):
        print ("---------------------------------")
        print ("      ***   PILOTOS    ***       ")
        print ("--------------------------------- \n")
        print (" (1) Añadir Piloto")
        print (" (2) Listar Pilotos")
        print (" (3) Borrar Piloto")
        print (" (4) Modificar Piloto")
        print (" (0) Volver al menu principal \n")
  
        op_menu = input ("Elija una opción:  ")
    
        if (op_menu == "0"):
            mostrar_menuprin()
        elif (op_menu == "1"):
            añadir_pilotos()
        elif (op_menu == "2"):
            listar_pilotos()
        elif (op_menu == "3"):
            eliminar_pilotos()
        elif (op_menu == "4"):
            modificar_piloto()
            
def menu_carreras ():
    
    while(True):
        print ("---------------------------------")
        print ("      ***  CARRERAS GP  ***     \n")
        print ("--------------------------------- \n")
        print (" (1) Añadir Carreras")
        print (" (2) Ver Lista de Carreras ")
        print (" (3) Borrar Carreras ")
        print (" (4) Modificar Carreras")
        print (" (5) Ver calendario previsto temporada")
        print (" (0) Volver al menu principal \n")
        
        op_menu = input ("Elija una opción:  ")
    
        if (op_menu == "0"):
            mostrar_menuprin()
        elif (op_menu == "1"):
            añadir_carreras()
        elif (op_menu == "2"):
            listar_carreras()
        #elif (op_menu == "3"):
          #  eliminar_eliminar()
        #elif (op_menu == "5"):
          # cargar_calendario()
    return



def menu_resultados():
    while(True):
        print ("------------------------------------------------------")
        print ("      ***  RESULTADOS Y CLASIFICACIONES  ***          ")
        print ("------------------------------------------------------")
        print (" (1) Registrar resultados")
        print (" (2) Clasificación de pilotos")
        print (" (3) Clasificación de equipos")
        print (" (4) Resultados por carrera")
        print (" (0) Volver al menu principal\n")

        op_menu = input("Elija una opción:  ")
    
        if (op_menu == "0"):
            mostrar_menuprin()
        elif (op_menu == "1"):
            registrar_resultados()
        elif (op_menu == "2"):
            calificacion_pilotos()
       # elif (op_menu == "3"):
           # listar_clasequipos()
    return

def obtener_puntaje_total(piloto_buscar):
    # acumulador
    puntaje_total = 0
    
    for posicion in lista_posiciones:
        if posicion["id_piloto"] == piloto_buscar["id"]:
            puntaje_total = puntaje_total + int(posicion["puntos"])

    return puntaje_total


def calificacion_pilotos():
    for piloto in lista_pilotos:
        puntaje_total = obtener_puntaje_total(piloto)

        print(piloto["nombre"] + " : " + str(puntaje_total) + " pts.")

def obtener_puntaje(posicion):
    if posicion == 1:
        return 25
    elif posicion == 2:
        return 18
    elif posicion == 3:
        return 15
    elif posicion == 4:
        return 10
    elif posicion == 5:
        return 8
    elif posicion == 6:
        return 6
    elif posicion == 7:
        return 5
    elif posicion == 8:
        return 3
    elif posicion == 9:
        return 2
    elif posicion == 10:
        return 1
    else:
        return 0
        
def registrar_resultados():
    mostrar_todo = False
    listar_carreras(mostrar_todo)

    id_carrera = int(input("Ingrese id de carrera: "))
    
    for piloto in lista_pilotos:
        posicion = int(input("Posición de " + piloto["nombre"] + ": "))

        posicion_diccionario = {}

        posicion_diccionario["id"] = (len(lista_posiciones)) + 1
        posicion_diccionario["id_carrera"] = id_carrera
        posicion_diccionario["id_piloto"] = piloto["id"]
        posicion_diccionario["posicion"] = posicion
        posicion_diccionario["puntos"] = obtener_puntaje(posicion)

        lista_posiciones.append(posicion_diccionario)

        guardar_cvs(POSICIONES_NOMBRE_ARCHIVO, lista_posiciones)

#FUNCIONES NIVES 3 (SUBMENUS)

#submenus pilotos--------------------------------------------------------------------------------
def listar_pilotos():
    print ("|-------------------------------------------------------------------------------------|")
    print ("|                         ***   LISTA DE PILOTOS    ***                               | ")
    print ("|-------------------------------------------------------------------------------------| \n")
    
    with open (PILOTOS_NOMBRE_ARCHIVO) as file:
        reader = csv.reader(file)
        for row in reader: 
            
            print ("{0:3} .-{2:8} |{1:<20} |{3:<15}|{4:<5} |{5:<5} ".format(row[0], row[1], row[2],row[3], row[4], row[5]))
            print ("--------------------------------------------------------------------------------------")
            
   # pause() 
       
    return     
  
def añadir_pilotos():
    newPiloto = {}
    
    print ("Pilotos existentes: " + str(len(lista_pilotos)))
    
    newPiloto["id"] = (len(lista_pilotos)) + 1
    newPiloto["nombre"] = input("Nombre del Piloto: ").title()
    newPiloto["siglas"] = input("Siglas Piloto (tres primeras letras del apellido): ").upper()
    newPiloto["pais"] = input("País: ").title()
    newPiloto["edad"] = input ("Edad:  ")
    newPiloto["equipo"] = input("Equipo: ").title()
    
    #evitar duplicados
    
    duplicado = False

    for old in lista_pilotos:
        if old["nombre"] == newPiloto["nombre"] or old["id"] == newPiloto["id"]:
            duplicado = True
            print ("\n")
            print ("\n")
            print ("\n")
            print ("El newPiloto introducido YA EXISTE!! \n")
            pause()
            break
    
    if duplicado == False:
        lista_pilotos.append(newPiloto)
        print ("\n")
        print ("Nuevo newPiloto REGISTRADO CON EXITO! \n")
    
    guardar_cvs(PILOTOS_NOMBRE_ARCHIVO, lista_pilotos) 

    return

          
def eliminar_pilotos():
    if(lista_pilotos.__len__() == 0):
        print("No hay pilotos que mostrar")
    else:
        print("-------------------------")
        print("Listado de pilotos")
        print("-------------------------")

        i = 1
        for j in lista_pilotos:
            print(str(i) + ".- " + j["nombre"])
            i += 1

        print(str(i) + ".- Volver")

        print("-------------------------")

        indice = int(input("Ingrese el número del newPiloto a eliminar:"))

        if (indice != i):
            indice = indice - 1

            while (True):
                resp = input("¿Realmente desea eliminar? [s/n]: ")
                resp = resp.lower()

                if (resp == "s" or resp == "n"):
                    break
                else:
                    print("Ingrese s ó n.")

            if (resp == "s"):
                lista_pilotos.pop(indice)
                print("Piloto eliminado!")

   
    guardar_cvs(PILOTOS_NOMBRE_ARCHIVO, lista_pilotos)
    return

def modificar_piloto ():
    if(lista_pilotos.__len__() == 0):
        print("No hay pilotos que mostrar")
    else:
        print("-------------------------")
        print("Listado de pilotos")
        print("-------------------------")

        i = 1
        for j in lista_pilotos:
            print(str(i) + ".- " + j["nombre"])
            i += 1

        print(str(i) + ".- Volver")

        print("-------------------------")

        indicem = int(input("Ingrese el número del newPiloto a modificar:"))

        if (indicem != i):
            indicem = indicem - 1

            while (True):
                resp = input("¿Realmente desea modificar? [s/n]: ")
                resp = resp.lower()

                if (resp == "s" or resp == "n"):
                    break
                else:
                    print("Ingrese s ó n.")

            if (resp == "s"):
                    lista_pilotos.pop(indicem)
                    print ("Inserte los nuevos datos: ")
                    newPiloto["nombre"]= input("Nombre del Piloto: ").title()
                    newPiloto["id"]= input("Identificador Piloto (tres primeras letras del apellido): ").upper()
                    newPiloto["pais"]= input("País: ").title()
                    newPiloto["edad"]= input ("Edad:  ")
                    newPiloto["equipo"]= input("Equipo: ").title()
                    lista_pilotos.insert(indicem, newPiloto)
                    print("Piloto modificado!")
    guardar_cvs(PILOTOS_NOMBRE_ARCHIVO, lista_pilotos) 
    
    return
#submenu carreras---------------------------------------------------------------------------
  
def añadir_carreras():
    carrera = {}
  
    print("Carreras existentes: " + str(len(lista_carreras)))
    
    carrera["id"] = (len(lista_carreras))+1
    carrera["nombre del gp"] = input("Nombre del Grán Premio: ").title()
    carrera["pais"] = input("País: ").title()
    carrera["circuito"] = input ("Nombre del circuito:  ").title()
    carrera["fecha"] = input("fecha: (ej. 02/05/2020) ")

    lista_carreras.append(carrera)
    print("Nuevo Gran Premio REGISTRADO CON EXITO! \n")
    
    guardar_cvs(CARRERAS_NOMBRE_ARCHIVO, lista_carreras) 
    return 
  
def listar_carreras(mostrar_todo = True):
    print ("|-------------------------------------------------------------------------------------|")
    print ("|                         ***   LISTA DE CARRERAS    ***                              | ")
    print ("|-------------------------------------------------------------------------------------| \n")
   
    with open (CARRERAS_NOMBRE_ARCHIVO) as file:
        reader = csv.reader(file)
        for row in reader: 
            if(mostrar_todo):
                print ("  {0:3} |{1:<30} |{2:<15}|{3:<20} |{4:<6} ".format(row[0], row[1], row[2],row[3], row[4]))
            else:
                print ("  {0:3} |{1:<30}  ".format(row[0], row[1]))     
            
            print ("--------------------------------------------------------------------------------------")
            
    pause()        
    return  

def registrar_resultados_backup():
    carrera = {} 
  
    listar_carreras()

    r = str(input("Inserte Id del Gran premio  :")) #conseguimos el id de carrera
    
    #iteramos lista de pilotos y añadimos un campo nuevo en cada diccionario de piloto     
    for piloto in lista_pilotos: #este capo sera la posición de cada piloto en la carrera
        pos= input("Inserte la POSICION FINAL de  "+ piloto["nombre"]+ ":")
        piloto["posicion_G_"+str(r)]=pos
        carrera["puntosGP_"+str(r)]=pos
            
        #iteramos lista de pilotos y añadimos un campo nuevo en cada diccionario de piloto     
            
    if piloto not in lista_pilotos:#evitamos duplicados
        lista_pilotos.append(piloto)   
        lista_resultados.append(carrera) 

    print(lista_resultados)
    guardar_cvs(PILOTOS_NOMBRE_ARCHIVO, lista_pilotos)

    return
#lo intente asi, pero no lo consigo
def convertir_puntos():
    lista_resultados = lista_pilotos
    carrera={}  
    for carrera in lista_resultados:
        for key in carrera.keys():
            if key ==({"posicion_GP_1":10}):
               carrera.update({"posicion_GP_1":100})
               lista_resultados.append(carrera)
 
def salir():
    guardar_cvs(PILOTOS_NOMBRE_ARCHIVO, lista_pilotos)
    guardar_cvs(CARRERAS_NOMBRE_ARCHIVO, lista_carreras)
    
    print("Agur" , nombre_usuario, ", espero haberte sido útil. Gracias por utilizarme")
    sys.exit()

def pause():
    input("Presione enter para continuar...")

def guardar_cvs(nombre_archivo, lista):
    with open (nombre_archivo, "w", newline='') as file:
        writer = csv.DictWriter(file, lista[0].keys())
        writer.writeheader()

        for objeto in lista:
            writer.writerow(objeto) 
    
    file.close()    

#----------------------PROGRAMA PRINCIPAL---------------------------------------
if TEST:
    nombre_usuario = "Pato"

    # abrimos el fichero csv de pilotos
    input_listapilotos = csv.DictReader(open(PILOTOS_NOMBRE_ARCHIVO))

    # cargamos los pilotos existentes en la lista de pilotos (lsta_pilotos)    
    for piloto in input_listapilotos:
        lista_pilotos.append(piloto)

    # abrimos el fichero csv de carreras
    input_listacarreras = csv.DictReader(open(CARRERAS_NOMBRE_ARCHIVO))

    # cargamos las carreras existentes (lista_carreras)    
    for carrera in input_listacarreras:
        lista_carreras.append(carrera)

    # abrimos el fichero csv de posiciones
    input_listaposiciones = csv.DictReader(open(POSICIONES_NOMBRE_ARCHIVO))

    # cargamos las posiciones existentes (lista_posiciones)    
    for posicion in input_listaposiciones:
        lista_posiciones.append(posicion)

    registrar_resultados()
    calificacion_pilotos()
else:    
    # definir nombre de nombre_usuario al arrancar programa
    print ("TECLEE SU NOMBRE: ")
    nombre_usuario = str(input ()).upper() 

    # abrimos el fichero csv de pilotos
    input_listapilotos = csv.DictReader(open(PILOTOS_NOMBRE_ARCHIVO))

    # cargamos los pilotos existentes en la lista de pilotos (lsta_pilotos)    
    for piloto in input_listapilotos:
        lista_pilotos.append(piloto)

    # abrimos el fichero csv de carreras
    input_listacarreras = csv.DictReader(open(CARRERAS_NOMBRE_ARCHIVO))

    # cargamos las carreras existentes (lista_carreras)    
    for carrera in input_listacarreras:
        lista_carreras.append(carrera)

    # POSICIONES_NOMBRE_ARCHIVO

    # abrimos el fichero csv de posiciones
    input_listaposiciones = csv.DictReader(open(POSICIONES_NOMBRE_ARCHIVO))

    # cargamos las posiciones existentes (lista_posiciones)    
    for posicion in input_listaposiciones:
        lista_posiciones.append(posicion)

    mostrar_bienvenida()
    pause()
    mostrar_menuprin()