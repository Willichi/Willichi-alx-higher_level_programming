#!/usr/bin/python3
def no_c(my_string):
    """
    a function that removes all characters c and C from a string.
    """
    copy =[x for x in my_string if x !='c' and x != 'C']
 
    return("".join(copy))
