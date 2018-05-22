# -*- coding: utf-8 -*-

if __name__ == '__main__':
    file_name = 'text_files/programming.txt'
    with open(file_name, 'a') as file_object:
        file_object.write("I also love finding meaning in large datasets.\n")
        file_object.write("I love creating apps that can run in a browser.\n")
