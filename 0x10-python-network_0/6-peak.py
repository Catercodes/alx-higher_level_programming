#!/usr/bin/python3
def find_peak(list_of_integers):
    max_num = 0;
    for i in list_of_integers:
        if list_of_integers[i] > max_num:
            max_num = list_of_integers
    return max_num
    
