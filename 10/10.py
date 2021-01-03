#!/usr/bin/python3

from collections import Counter


def part1(adapters):
    diffs = [adapters[i] - adapters[i - 1] for i in range(1, len(adapters))]
    c = Counter(diffs)
    return c[1] * c[3]


def count_combinations(adapters):
    cache = [None] * len(adapters)

    def _count_combinations_to_reach(i):
        if i == 0:
            return 1
        ret = 0
        j = i - 1
        while j >= 0 and adapters[i] - adapters[j] <= 3:
            if not cache[j]:
                cache[j] = _count_combinations_to_reach(j)
            ret += cache[j]
            j -= 1
        return ret

    return _count_combinations_to_reach(len(adapters) - 1)


if __name__ == "__main__":
    with open("input") as f:
        adapters = [int(j) for j in f.read().splitlines()]
        adapters.append(0)
        adapters.append(max(adapters) + 3)
        adapters.sort()

        result1 = part1(adapters)
        print("Result of part1 is {}".format(result1))

        n_combinations = count_combinations(adapters)
        print("{} distinct combinations".format(n_combinations))
