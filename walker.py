import os
from datetime import datetime
import time
import csv
from methods import *


def main():
    valido = False
    now = datetime.now()
    inicio_algoritmo = time.time()

    print("*******************************************************")
    print('\t\t\t\t Gestión de inventarios')
    print("*******************************************************")

    while not valido:

        print("Ingrese una de las siguientes opciones: "
              "\n\tC - Para crear inventario de carpetas "
              "\n\tA - Para crear inventario de archivos "
              "\n\tX - Para crear inventario de carpetas y archivos"
              "\n\tL - Para leer un archivo CSV")

        option = input('--> : ')
        valido = validate_input(option)

        if option in ['C', 'c']:
            # num_path = int(input('Ingrese la cantidad de rutas que desea leer: '))
            #
            # if num_path == 1:
            path = input('Ingrese la ruta que desea MAPEAR: ')
            generado = folders_inventory(path)
            generado += '.csv'
            # print(f'Se ha creado el archivo "{generado}" por favor ábrelo y modifica la columna "Rename" con el '
            #       f'nuevo nombre y guárdalo.')

            # confirm = input('Presiona S cuando guardes el archivo y estés listo para renombrar los folders: ')

            # if confirm in ['S', 's', 'SI', 'si', 'Si']:
            # with open(generado) as f:
            #     reader = csv.DictReader(f)
            #
            #     for row in reader:
            #         os.rename(row['Path'], row['Rename'])

            print('\nHemos finalizado, por favor revisa. Gracias.')


        elif option in ['A', 'a']:
            files_inventory(path)
        if option in ['X','x']:
            num_path = int(input('Ingrese la cantidad de rutas que desea leer: '))

            if num_path == 1:
                path = input('Ingrese la ruta que desea MAPEAR: ')
                items = validate_list(folders_files_inventory(path))

                generated_file = 'folder_items_inv'
                keys = ['Path']
                generate_csv(generated_file, keys, items)

                print(f'Se ha creado el archivo "{generated_file}.csv"')

                # confirm = input('Presiona S cuando guardes el archivo y estés listo para renombrar los folders: ')

                # if confirm in ['S', 's', 'SI', 'si', 'Si']:
                # with open(generado) as f:
                #     reader = csv.DictReader(f)
                #
                #     for row in reader:
                #         os.rename(row['Path'], row['Rename'])

                print('\nHemos finalizado, por favor revisa. Gracias.')

            elif num_path == 2:

                path1 = input('Ingrese la primera ruta que desea MAPEAR: ')
                path2 = input('Ingrese la segunda ruta que desea MAPEAR: ')

                items1 = folders_files_inventory(path1)
                items2 = folders_files_inventory(path2)

                keys = ['Path1', 'Path2']

                # print(items)
                generated_file = 'folder_items_inv'

                generate_csv(generated_file, keys, items1, items2)

                print(f'Se ha creado el archivo "{generated_file}.csv"')

        if option in ['L','l']:
            print('SIUUUUUU')
            # filename = input('Ingresa el nombre del archivo que deseas leer:')
            # with open(filename+'.csv') as f:
            #     reader = csv.DictReader(f)
            #
            #     for row in reader:
            #         os.rename(row['DsPetro'], row['Rename'])

        else:
            print('La opción ingresada es incorrecta. Vuelve a intentarlo.\n')

    fin_algoritmo = time.time()
    print(f'\n<<<<<<<<<<<<<<<< Tiempo total de algoritmo: {fin_algoritmo - inicio_algoritmo} >>>>>>>>>>>>>>>>\n')


if __name__ == "__main__":
    main()