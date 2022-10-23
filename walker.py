from datetime import datetime
import time
from methods import *
from glob import glob


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

        elif option in ['X','x']:
            num_path = int(input('Ingrese la cantidad de rutas que desea leer (máximo 2): '))
            # num_path = 2

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
                # path1 = "C:\\Users\\H268497\\Downloads\\TESTING\\IP"
                path2 = input('Ingrese la segunda ruta que desea MAPEAR: ')
                # path2 = "C:\\Users\\H268497\\Downloads\\TESTING\\DSPetro"

                folderList1 = folders_files_inventory(path1)
                folderList2 = folders_files_inventory(path2)

                # folderList1.sort(key=len)
                # folderList2.sort(key=len)

                # print("Lista 1",folderList1)
                # print("\nLista 2",folderList2)

                joinedList = compare_name_values(folderList1, folderList2)

                print("\n****************** Lista de elementos [IP, DSPETRO] ******************\n\n",joinedList,"\n")
                #
                folderList2 = folders_files_inventory(path2, True)

                # print("\n Nueva Lista 2", folderList2)

                rename = folderList2.copy()

                sub = dict(joinedList)

                # print(f'{sub}')

                for key, val in sub.items():
                    # print('=====================================')
                    # print(f'{key} ----- {val}')
                    for idx, ele in enumerate(folderList2):
                        if val in ele:
                            # print(f'******* {idx} **** {ele}')
                            rename[idx] = ele.replace(val, key)
                    # print('=====================================')

                keys = ['Path2', 'Rename']
                generated_file = 'file_migration'
                try:
                    generate_csv(generated_file, keys, folderList2,rename)
                    print(f'Se ha creado el archivo "{generated_file}.csv"')

                    confirm = input('Revisa el archivo y presiona S cuando estés listo para renombrar: ')

                    if confirm in ['S', 's', 'SI', 'si', 'Si']:
                        with open(generated_file+'.csv') as f:
                            reader = csv.DictReader(f)

                            for row in reader:
                                os.rename(row['Path2'], row['Rename'])

                    print('\nHemos finalizado, por favor revisa. Gracias.')
                except:
                    print("NO SE PUDO GENERAR AL ARCHIVO, SEGURO TIENE UNO CON ABIERTO, CREADO CON ANTERIORIDAD EN LA MISMA CARPETA.")
                    print("\nCIERRELO E INTENTE NUEVAMENTE.")

        elif option in ['L','l']:
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