#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boolist = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            boolist[count] = True
        else:
            boolist[count] = False
    return(boolist)

vi 11-delete_at.py

#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        del(my_list[idx])
    return(my_list)
