# -*- coding: utf-8 -*-


def count_words(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = '*****ERROR:Sorry, the file ' + filename + ' does not exist.'
        print(msg)
        return -1
    else:
        words = contents.split()
        num_words = len(words)
        return num_words


if __name__ == '__main__':
    # file_name = 'files/alice.txt'
    file_names = ['files/alice.txt', 'files/siddhartha.txt', 'files/moby_dict.txt', 'files/little_women.txt']
    for file_name in file_names:
        count = count_words(file_name)
        if count != -1:
            print("The file " + file_name + " has about " + str(count) + " words.")

