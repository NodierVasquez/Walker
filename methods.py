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

def folders_files_inventory(path: str, condition: bool = False, divider: str = None):

    '''
    Find all files and folders inside given path.

    :param path: Path to walk
    :param condition: When this variable is True, the script read all files on path
    :param divider: String divider to avoid errors when rename
    :return: List of string that contain all inside path
    '''

    if condition:
        items = glob(path + "/**")
    else:
        items = glob(path+"/Well*")
        print('=============================================')
        copy = []
        for i in items:
            if not 'Copy of' in i or not 'Copy' in i:
                copy.append(i)
        items = copy[:]
        print(f'HEMOS ENCONTRADO: {len(items)} ITEMS EN {path}\n')
        print(items)
        print('=============================================')

    return items

def rename_files(path, option: int = 0):
    '''
    Rename all files and folders inside given path, to avoid
    Errors when rename using CSV file.

    :param path: Path to walk
    :param option: Number of format that the user want
    :return: List of string that contain all inside path
    '''


    for item in glob(path + "/**"):
        if "Well" in item or "IPDWell" in item:
            if option == 1 and not "Well-" in item:
                os.rename(item, item.replace("Well","Well-"))
            elif option == 2:
                os.rename(item, item.replace("Well-","Well"))
            else:
                print("\nNo se pueden renombrar los archivos.\n")

    items = glob(path + "/**")

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


def generate_csv(generated_file:str, keys:list, files:list, files2=[], files3=[]):
    '''
    Generate a CSV file with paths that was reading before.

    :param generated_file: Custom name for CSV file that will be generated.
    :param keys: List with names of columns.
    :param files: List of paths.
    :param files2: Optional parameter if you can read second path
    :return: None
    '''
    if not files2:
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

def compare_name_values(folderList1: list, folderList2: list):
    '''
    Extract split name of folders in *folderList1* and then comparing
    those values in *folderList2* and use them to create a new list.

    :param folderList1: List with the paths that we need to iterate
    :param folderList2: List with the path that we need to compare using folderList1
    :return: List with join values between .*folderList1* and *folderList2*
    '''

    values = []

    print("\n************ INFORMACIÓN ENCONTRADA **************\nEstructura:")
    print(f'\tIP\n\t\tDSPETRO')
    print("*********************************************")
    for item in folderList1:
        if os.path.isdir(item):
            ipFilename = os.path.basename(item)
            print(f'\t{ipFilename}')
            if 'Well' in ipFilename:
                splitIPFilename = ipFilename.split()

                for item2 in folderList2:
                    if splitIPFilename[1] in item2:
                        dsFilename = os.path.basename(item2)
                        splitDSFilename = dsFilename.split()

                        if splitIPFilename[1] == splitDSFilename[1]:
                            print(f'\t\t{dsFilename} ')
                            list = []
                            list.append(splitDSFilename[0])
                            list.append(splitIPFilename[0])
                            values.append(list)

    return values

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