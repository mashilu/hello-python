# -*- coding: utf-8 -*-


def get_formatted_name(first, last, middle=''):
    """
    Generate a nearly fromated full name.
    :param first:
    :param last:
    :param middle:
    :return:
    """
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()

