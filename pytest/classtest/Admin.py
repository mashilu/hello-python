# -*_ coding: utf-8 -*-
from pytest.classtest.User import User
from pytest.classtest.Privileges import Privileges


class Admin(User):

    def __init__(self, first_name, last_name, **attr):
        super().__init__(first_name, last_name, **attr)
        self.privileges = Privileges()


if __name__ == '__main__':
    a_admin = Admin('ma', 'shilu')
    a_admin.privileges.show_privileges()
