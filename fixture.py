# -*- coding: utf-8 -*-
# Importando librerías
import sys
import pickle

sys.path.append("python-modules")

from tools.validate.validate import *
from tools.view.view import *


# Validando la existencia de los archivos
validating_existence_file("equipos.dat")
equipos = loading_file_into_memory("equipos.dat")

# Definición de funciones
def menu_principal():
    cleaning()
    print "\nFixture y prediccion.\n\nMenú Principal.\n\n"
    print "\n\t1. Acceder como administrador."
    print "\n\t2. Registrar usuario nuevo."
    print "\n\t3. Ingresar como usuario existente."
    print "\n\t4. Salir."
    opcion = raw_input("\n\n\t\tIngrese una opción: ")
    opcion = validate_integer(opcion)
    opcion = validate_range(opcion, 1, 4)
    return opcion

def menu_administrador():
    cleaning()
    print "\nMenú administrador.\n\n"
    print "\n\t1. Ingresar equipos."
    print "\n\t2. Modificar equipos."
    print "\n\t3. Cargar resultado."
    print "\n\t4. Modificar resultado."   
    print "\n\t5. Retornar al Menú Principal."
    opcion = raw_input("\n\n\t\tIngrese una opción: ")
    opcion = validate_integer(opcion)
    opcion = validate_range(opcion, 1, 5)
    return opcion
    
def menu_usuario():
    cleaning()
    print "\nMenú Usuario.\n\n"
    print "\n\t1. Ver resultados."
    print "\n\t2. Hacer prediccion."
    print "\n\t3. Resultados de prediccion."
    print "\n\t4. Eliminar usuario."
    print "\n\t5. Retornar al Menú Principal."
    opcion = raw_input("\n\n\t\tIngrese una opción: ")
    opcion = validate_integer(opcion)
    opcion = validate_range(opcion, 1, 5)
    return opcion
    
def ingresar_usuario(base):
    cleaning()
    print "\nRegistrarse.\n\n"
    user = raw_input("\n\t\tIngrese el nombre de USUARIO: ")
    if user not in base.keys():
        print "\n\tRellene los campos con la información correspondiente al USUARIO.\n"
        temporal = []
        dato = raw_input("\n\t\t1. Nombre(s): ")
        temporal.append(dato)
        dato = raw_input("\n\t\t2. Apellido(s): ")
        temporal.append(dato)
        dato = raw_input("\n\t\t3. Contraseña: ")
        temporal.append(dato)
        base[user] = temporal
        cleaning()
        print "\n\t\tEl USUARIO ha sido registrado exitosamente."
    else:
        print "\n\t\tEl usuario existente."
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")
    
def modificar_usuario(base):
    cleaning()
    print "\nModificar usuario.\n\n"
    user = raw_input("\n\t\tIngrese el nombre de usuario a modificar: ")
    cleaning()
    if user in base.keys():
        temporal = base[user]
        print "\nLos datos del usuario", user, "a modificar son:\n"
        print "\n\t\t1. Apellido(s):", temporal[0]
        print "\n\t\t2. Nombre(s):", temporal[1]
        print "\n\t\t3. Contrseña:", temporal[2]
        print "\n\n\n\t\t4. Salir SIN MODIFICAR DATOS del CLIENTE."
        atributo = raw_input("\n\n\t\tIngrese una opción: ")
        atributo = validate_integer(atributo)
        atributo = validate_range(atributo, 1, 4)
        cleaning()
        if atributo != 4:
            msje = "Ingrese "
            etiquetas = ["Apellido(s): ", "Nombre(s): ", "Contraseña: "]
            msje = msje + etiquetas[atributo - 1]
            dato = raw_input(msje)
            temporal[atributo - 1] = dato
            base[user] = temporal
            cleaning()
            print "\n\t\tUsuario modificado exitosamente."
        else:
            print "\n\t\tNO ha modificado el usuario."
    else:
        print "\nEl usuario", user, "que desea modificar, NO ESTÁ REGISTRADO.\n"
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")

def eliminar_usuario(base):
    cleaning()
    print "\nEliminar Usuario.\n\n"
    user = raw_input("\n\t\tIngrese el nombre de usuario que desea eliminar: ")
    password = raw_input("\n\t\tIngrese la contraseña: ")
    password = validate_password(password)
    cleaning()
    if user in base.keys() and password == user[2]:
        del base[user]
        cleaning()
        print "\n\t\tUSUARIO ELIMINADO."
    else:
        print "\nEl USUARIO", user, "no existe.\n"
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")


"""

def prueba(base):
    temporal = []
    codigo_equipo = raw_input("ingrse codigo de equipo")
    agregar = raw_input("ingrse equipo")
    temporal.append(agregar)
    base[codigo_equipo] = temporal
    saving_changes_to_the_file("equipos.dat", equipos)
prueba(equipos)
print equipos
"""
menu_principal()