#!/usr/bin/python3

indices_to_print = [2020, 30000000]

if __name__ == "__main__":
    _input = open("input").read().rstrip()
    queue = [int(i) for i in _input.split(",")]
    print(queue)

    last_spoken_by_num = {}

    for i in range(max(indices_to_print)):
        num = queue.pop(0)

        if i + 1 in indices_to_print:
            print("Number {} is {}".format(i + 1, num))

        if not queue:
            try:
                last_spoken = last_spoken_by_num[num]
                next_num = i - last_spoken
            except KeyError:
                next_num = 0
            queue.append(next_num)

        last_spoken_by_num[num] = i
