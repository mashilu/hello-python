# -*- coding: utf-8 -*-
class User:

    def __init__(self, first_name, last_name, **attr):
        self.first_name = first_name
        self.last_name = last_name
        self.attr = dict()
        for key, value in attr.items():
            self.attr[key] = value

    def describe_user(self):
        print(self.first_name)
        print(self.last_name)
        for key, value in self.attr.items():
            print(key + "=" + value)

    def greet_user(self):
        print("hello, " + self.first_name + " " + self.last_name)


if __name__ == '__main__':
    user = User("ma", "shilu", job="test engineer", sex="male")
    user.describe_user()
    user.greet_user()
