#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    a function that deletes the item at a specific position in a list
    """
    if idx < 0 :
      return my_list
    elif idx > len(my_list) - 1:
      return my_list
    pop = [ x for x in my_list]
        del my_lisf(idx)
    return my_list
