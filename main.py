import os.path
from datetime import datetime
import time
import csv

def main():
    now = datetime.now()
    inicio_algoritmo = time.time()

    path = input('Ingrese la ruta que desea MAPEAR:\n')

    files = []
    rows = []
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

    print(f'ARCHIVOS ENCONTRADOS: {len(files)}')

    generated_file = input('Ingresa el nombre del Archivo:\n')

    keys = ['Path', 'Base', 'Folder', 'Filemane']

    with open(f'{generated_file}.csv', 'w', encoding="utf-8", newline='') as output_file:
        dict_writer = csv.writer(output_file)
        dict_writer.writerow(keys)
        dict_writer.writerows(files)

    fin_algoritmo = time.time()
    print(f'\n<<<<<<<<<<<<<<<< Tiempo total de algoritmo: {fin_algoritmo - inicio_algoritmo} >>>>>>>>>>>>>>>>\n')

if __name__ == "__main__":
    main()