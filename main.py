import os
from datetime import datetime
import time
import csv

def main():
    valido = False
    now = datetime.now()
    inicio_algoritmo = time.time()

    path = input('Ingrese la ruta que desea MAPEAR: ')

    while not valido:

        dato = int(input('Ingrese (número): 1 Para leer solo carpetas y luego renombrar o 2 Para leer archivos: '))
        valido = validate_input(dato)
        if dato == 1:
            generado = read_folders_to_rename(path)
            generado += '.csv'
            print(f'Se ha creado el archivo "{generado}" por favor ábrelo y modifica la columna "Rename" con el nuevo nombre y guárdalo.')

            confirm = input('Presiona S cuando guardes el archivo y estés listo para renombrar los folders: ')

            if confirm in ['S', 's', 'SI', 'si', 'Si']:
                with open(generado) as f:
                    reader = csv.DictReader(f)

                    for row in reader:
                        os.rename(row['Path'], row['Rename'])

            print('\nHemos finalizado, por favor revisa. Gracias.')

        elif dato == 2:
            files_inventory(path)
        else:
            print('En número ingresado es incorrecto. Vuelve a intentarlo.\n')


    fin_algoritmo = time.time()
    print(f'\n<<<<<<<<<<<<<<<< Tiempo total de algoritmo: {fin_algoritmo - inicio_algoritmo} >>>>>>>>>>>>>>>>\n')

def read_folders_to_rename(path):
    files = []
    i = 1
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for folder in d:
            row = []
            fullpath = os.path.join(r, folder)
            row.append(fullpath)
            files.append(row)
            i += 1

    print(f'HEMOS ENCONTRADO: {len(files)} FOLDERS')

    generated_file = 'rename_folder'
    keys = ['Path', 'Rename']
    generate_csv(generated_file, keys, files)

    return generated_file

def files_inventory(path):
    files = []
    i = 1
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):

        for file in f:
            row = []
            fullpath = os.path.join(r, file)
            parent_folder = r.split('\\')[-1]
            row.append(fullpath)
            row.append(os.path.dirname(fullpath))
            row.append(parent_folder)
            row.append(file)

            files.append(row)
            i += 1

    print(f'HEMOS ENCONTRADO: {len(files)} ARCHIVOS')

    generated_file = input('Ingresa el nombre del Archivo:\n')
    keys = ['Path', 'Base', 'Folder', 'Filemane']
    generate_csv(generated_file,keys,files)

def generate_csv(generated_file, keys, files):
    with open(f'{generated_file}.csv', 'w', encoding="utf-8", newline='') as output_file:
        dict_writer = csv.writer(output_file)
        dict_writer.writerow(keys)
        dict_writer.writerows(files)

def validate_input(value):
    if value in [1, 2]:
        return True
    return False

if __name__ == "__main__":
    main()