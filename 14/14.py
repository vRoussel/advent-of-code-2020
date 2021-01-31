#!/usr/bin/python3

import math
import re

MASK_RE = re.compile(r"^mask *= *([01X]+)$")
WRITE_RE = re.compile(r"^mem\[(\d+)\] *= *(\d+)$")

set_bitmask = None
reset_bitmask = None
mem = {}


def update_bitmask(mask):
    global set_bitmask, reset_bitmask
    set_bitmask = int(mask.replace("X", "0"), 2)
    reset_bitmask = int(mask.replace("X", "1"), 2)
    # print("{:036b}".format(set_bitmask))
    # print("{:036b}".format(reset_bitmask))


if __name__ == "__main__":
    with open("input") as f:
        for line in f:
            line = line.rstrip()
            print(line)

            match = MASK_RE.fullmatch(line)
            if match:
                (bitmask,) = match.groups()
                update_bitmask(bitmask)
                continue

            match = WRITE_RE.fullmatch(line)
            if match:
                index, value = match.groups()
                index = int(index)
                value = int(value)
                masked_value = (value | set_bitmask) & reset_bitmask
                mem[index] = masked_value
        part1 = sum(mem.values())
        print("Sum of values for part1 is {}".format(part1))
