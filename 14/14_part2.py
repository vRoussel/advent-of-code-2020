#!/usr/bin/python3

import math
import re
from itertools import combinations, chain

MASK_RE = re.compile(r"^mask *= *([01X]+)$")
WRITE_RE = re.compile(r"^mem\[(\d+)\] *= *(\d+)$")

set_bitmask = None
floating_bits = []
mem = {}


def as_bin(i):
    return "{:036b}".format(i)


def update_bitmask(mask):
    global set_bitmask, floating_bits
    set_bitmask = int(mask.replace("X", "0"), 2)
    floating_bits = [i for (i, v) in enumerate(reversed(mask)) if v == "X"]
    print(floating_bits)
    # print("{:036b}".format(set_bitmask))


def all_possible_index(masked_index):
    if not floating_bits:
        yield masked_index

    # Reset all floating bits to 0
    for b in floating_bits:
        shifted = 0x1 << b
        flipped = ~shifted
        masked_index &= flipped

    tmp = (combinations(floating_bits, size) for size in range(len(floating_bits) + 1))
    bits_combinations = chain(*tmp)
    for bits in bits_combinations:
        this_index = masked_index
        for b in bits:
            this_index |= 0x1 << b
        yield this_index


def write(index, value):
    masked_index = index | set_bitmask
    for possible_index in all_possible_index(masked_index):
        mem[possible_index] = value


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
                write(index, value)

        part2 = sum(mem.values())
        print("Sum of values for part2 is {}".format(part2))
