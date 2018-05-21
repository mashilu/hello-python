# -*- coding: utf-8 -*-

if __name__ == '__main__':
    file_name = 'text_files/programming.txt'
    with open(file_name, 'w') as file_object:
        file_object.write("I love programming.")
