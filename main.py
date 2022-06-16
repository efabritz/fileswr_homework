# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pprint import pprint
import os


def make_cook_book(file_name):
    cook_book = {}
    with open(file_name) as file:
        for line in file:
            recipie_name = line.strip('\n')
            lines_amount = file.readline()
            ingridients = []
            for _ in range(int(lines_amount)):
                ingr_line = file.readline()
                ingr_splitted = ingr_line.split('|')
                ingridients.append({'ingridient_name' : ingr_splitted[0], 'quantity' : ingr_splitted[1], 'measure' : ingr_splitted[2].strip('\n')})
            cook_book[recipie_name] = ingridients
            file.readline()
    return cook_book

cook_book_file = 'recipies.txt'
pprint(make_cook_book(cook_book_file))

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = make_cook_book(cook_book_file)
    res_dict = {}
    for dish in dishes:
        for recipie in cook_book.keys():
            if dish == recipie:
                ingr_list = cook_book[recipie]
                for ingridient in ingr_list:
                    quantity_origin = 0
                    measure = ingridient['measure']
                    quantity = int(ingridient['quantity'])
                    if ingridient['ingridient_name'] in res_dict:
                        quantity_origin = res_dict[ingridient['ingridient_name']]['quantity']
                    inner_res_dict = {'measure': measure, 'quantity': quantity * person_count + quantity_origin}
                    res_dict[ingridient['ingridient_name']] = inner_res_dict

    return res_dict

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

def txt_to_file():
    base_path = os.getcwd()
    dir_name = 'texts'
    path_to_cataloge = os.path.join(base_path, dir_name)
    files_list = os.listdir(path_to_cataloge)
    write_file = os.path.join(path_to_cataloge, "res_file.txt")
    cont_dict = {}
    len_dict = {}
    for file_name in files_list:
        file_path = os.path.join(path_to_cataloge, file_name)
        with open(file_path) as f_obj:
            contents = f_obj.readlines()
            len_dict[file_name] = len(contents)
            cont_dict[file_name] = ''.join(contents)
    f_lst = sorted(len_dict, key=len_dict.get)
    with open(write_file, 'w') as wfile:
        for elem in f_lst:
            wfile.write(elem + "\n")
            wfile.write(str(len_dict[elem]) + "\n")
            wfile.write(cont_dict[elem] + "\n")

txt_to_file()

