# -*- coding: utf-8 -*-

from json import load

if __name__ == '__main__':
    file_name = 'text_files/numbers.json'
    with open(file_name) as file_obj:
        numbers = load(file_obj)
    print(numbers)

