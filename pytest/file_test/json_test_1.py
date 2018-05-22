# -*- coding: utf-8 -*-

from json import dump

if __name__ == '__main__':
    numbers = [2, 3, 5, 7, 11, 13]
    file_name = 'text_files/numbers.json'
    with open(file_name, 'w') as file_obj:
        dump(numbers, file_obj)
