#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        for i in my_list:
            if idx == my_list.index(i):
                my_list.remove(i)
                my_list.insert(idx, element)
                return my_list
