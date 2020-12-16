#!/usr/bin/python3

import re

r = re.compile(r'^(\d+)-(\d+) (\w+?): (\w+)$')

def check_first_policy(line):
    res = r.match(line.rstrip())
    try:
        _min, _max, _char, _pattern = res.groups()
        _min = int(_min)
        _max = int(_max)

        count = _pattern.count(_char)
        if _min <= count and count <= _max:
            return True
    except:
        print("(1)Unable to parse {}".format(line))
    return False

def check_second_policy(line):
    res = r.match(line.rstrip())
    try:
        i, j, _char, _pattern = res.groups()
        i = int(i)
        j = int(j)

        return (_pattern[i-1] == _char) ^ (_pattern[j-1] == _char)
    except:
        print("(2)Unable to parse {}".format(line))
    return False

if __name__ == '__main__':
    n_valid_first = 0
    n_valid_second = 0
    with open("input") as f:
        for line in f:
            if check_first_policy(line):
                n_valid_first += 1
            if check_second_policy(line):
                n_valid_second += 1
    print("{} valid password following first policy".format(n_valid_first))
    print("{} valid password following second policy".format(n_valid_second))
