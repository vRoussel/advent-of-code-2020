#!/usr/bin/python3

import sys

MAGIC_NUMBER = 2020

def find_two(sorted_input, magic_number):
    i = 0
    j = len(sorted_input) - 1
    while i < j:
        my_sum = sorted_input[i] + sorted_input[j]
        if my_sum > magic_number:
            j -= 1
        elif my_sum < magic_number:
            i += 1
        else:
            a = sorted_input[i]
            b = sorted_input[j]
            return (a,b)
    return None

def find_three(sorted_input, magic_number):
    for n in sorted_input:
        try:
            a,b = find_two(sorted_input, magic_number - n)
            return (a,b,n)
        except:
            pass


if __name__ == '__main__':
    with open('input') as f:
        raw_in = f.read()
        sorted_nums = sorted((int(i) for i in raw_in.splitlines()))
        try:
            a,b = find_two(sorted_nums, 2020)
            print('{} + {} = {} '.format(a, b, a+b))
            print('{} * {} = {} '.format(a, b, a*b))
        except:
            print("Unable to find 2 numbers")

        try:
            a,b,c = find_three(sorted_nums, 2020)
            print('{} + {} + {} = {} '.format(a, b, c, a+b+c))
            print('{} * {} * {} = {} '.format(a, b, c, a*b*c))
        except:
            print("Unable to find 3 numbers")

