#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    A function that reverse integers in my list
    """
    
    if my_list == None:
      return None
    for i in my_list[::-1]:
       print("{:d}".format(my_list[i]))
