#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    A function that prints integers in my_list.
    """

    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
