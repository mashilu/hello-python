# -*- coding: utf-8 -*-

if __name__ == '__main__':
    with open('text_files/pi_digits.txt') as file_object:
        lines = file_object.readlines()

    pi_string = ''
    for line in lines:
        pi_string += line.rstrip().lstrip()

    print(pi_string)
    print(len(pi_string))

