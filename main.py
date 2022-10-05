from poo import *
import os


def menu():
    funciones = Funciones()
    bolena = True
    while (bolena):
        MENU = int(input(f'''
         {'MEnu'.center(50, '-')}
         1-Ver usuarios.
         2-Agregar usuarios.
         3-Editar usuarios,
         4-Eliminar usuarios.
         5-SALIR
         Elije una opcion del menu:'''))
        os.system('cls')
        if MENU == 1:
            print(funciones.verDatos())
            os.system('pause')
            os.system('cls')
        elif MENU == 2:
            print(funciones.ingresa())
        elif MENU == 3:
            print(funciones.actualiza())
        elif MENU == 4:
            print(funciones.Eliminar())
        elif MENU == 5:
            print('Gracias por preferirnos')
            bolena = False
        else:
            print('Elige un opción del menú.')

    os.system('pause')
    os.system('cls')


menu()
