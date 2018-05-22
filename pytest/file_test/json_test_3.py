# -*- coding: utf-8 -*-

from json import dump
from json import load

if __name__ == '__main__':
    file_name = 'text_files/10-11.txt'
    number = int(input("please input a number, I'll remember it for you: "))
    with open(file_name, 'r+') as file_obj:
        dump(number, file_obj)
        print(load(file_obj))
