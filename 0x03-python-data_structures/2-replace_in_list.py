#!/usr/bin/python
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        my_list.remove(idx + 1)
        my_list.insert(idx, element)
        return my_list