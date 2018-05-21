# -*- coding: utf-8 -*-

if __name__ == '__main__':
    file_name = 'text_files/pi_digits.txt'

    # 打印时读取整个文件
    with open(file_name) as file_object:
        contents = file_object.read()
        print(contents)

    print("==================")

    # 打印时遍历文件对象
    with open(file_name) as file_object:
        for line in file_object:
            print(line.rstrip())

    print("==================")
    with open(file_name) as file_object:
        lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())