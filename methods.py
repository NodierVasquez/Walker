import os
from glob import glob
import csv

def folders_inventory(path):
    folders = []
    i = 1
    # r=root, d=directories, f = filas
    for r, d, f in os.walk(path):
        for dir in d:
            row = []
            fullpath = os.path.join(r, dir)
            row.append(fullpath)
            folders.append(row)
            i += 1

    print(f'HEMOS ENCONTRADO: {len(folders)} CARPETAS')

    generated_file = 'rename_folder'
    keys = ['Path', 'Rename']
    generate_csv(generated_file, keys, folders)

    return generated_file

def folders_files_inventory(path):

    items = glob(path+"/*")
    # items = []
    # for e in list_files:
    #     # row = {column: e}
    #     row = []
    #     row.append(e)
    #     items.append(row)

    print(f'HEMOS ENCONTRADO: {len(items)} ITEMS EN {path}')

    # generated_file = 'folder_items_inv'
    # keys = ['Path', 'Rename']
    # generate_csv(generated_file, keys, items)

    return items


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

    generated_file = input('Ingresa el nombre del Archivo: ')
    keys = ['Path', 'Base', 'Folder', 'Filemane']
    generate_csv(generated_file, keys, files)


def generate_csv(generated_file, keys, files, files2=[]):
    if  not files2:
        with open(f'{generated_file}.csv', 'w', encoding="utf-8", newline='') as output_file:
            dict_writer = csv.writer(output_file)
            dict_writer.writerow(keys)
            dict_writer.writerows(files)
    else:
        with open(f'{generated_file}.csv', 'w', encoding="utf-8", newline='') as output_file:
            dict_writer = csv.writer(output_file)
            dict_writer.writerow(keys)
            for item in zip(files, files2):
                dict_writer.writerow(item)


def validate_list(items):
    list = []
    for item in items:
        row = []
        row.append(item)
        list.append(row)
    return list

def validate_input(value):
    if value in ['C', 'c', 'A', 'a', 'X', 'x']:
        return True