#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    loop = 0
    try:
        for i in range(x):
            print("{:d}" .format(my_list[i]), end="")
            loop += 1
        print()
        return loop
    except IndexError:
        print()
        return i
