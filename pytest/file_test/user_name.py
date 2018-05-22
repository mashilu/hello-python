# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # user_name = input("please input your name: ")
    # file_name = 'text_files/guest.txt'
    # with open(file_name, 'a') as file_object:
    #     file_object.write(user_name + '\n')

    file_name = 'text_files/guest.txt'
    with open(file_name, 'a') as file_object:
        while True:
            user_name = input("input your name, XO to exit:")
            if user_name == 'XO':
                break
            else:
                print("Hello " + user_name + ". Nice to meet you")
                file_object.write(user_name + '\n')

