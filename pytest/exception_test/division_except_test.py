# -*- coding: utf-8 -*-

if __name__ == '__main__':
    while True:
        mode = input("Input a division calculated mode, like a/b, I will return the result. Enter 'q' to exit:")
        if mode == 'q':
            break
        numbers = mode.split('/')
        try:
            answer = int(numbers[0])/int(numbers[1])
        except ZeroDivisionError:
            print("You can't divide by 0! Please re-input ")
        except ValueError:
            print("Only digits allowed, please re-input")
        else:
            print(answer)
