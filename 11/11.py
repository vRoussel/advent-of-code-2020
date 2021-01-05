#!/usr/bin/python3

import copy

# Note: These two functions should be classes


def count_eventually_occupied_seats_model1(orig_seats):
    def _count_neighboors(_seats, row, col):
        neighboors = [
            (i, j)
            for i in range(row - 1, row + 2)
            for j in range(col - 1, col + 2)
            if (i, j) != (row, col)
        ]
        n_neighboors = 0
        for (i, j) in neighboors:
            if i < 0 or j < 0:
                continue
            try:
                if _seats[i][j] == "#":
                    n_neighboors += 1
            except:
                pass
        return n_neighboors

    def _forward(_seats):
        new_seats = copy.deepcopy(_seats)
        for i in range(len(_seats)):
            for j in range(len(_seats[i])):
                n_neighboors = _count_neighboors(_seats, i, j)
                current = _seats[i][j]
                if current == "L" and n_neighboors == 0:
                    new = "#"
                elif current == "#" and n_neighboors >= 4:
                    new = "L"
                else:
                    continue
                new_seats[i][j] = new
        # print("=== new_seats ===")
        # print("\n".join(["".join(line) for line in new_seats]))
        if new_seats == _seats:
            return sum([r.count("#") for r in _seats])
        else:
            return _forward(new_seats)

    return _forward(orig_seats)


def count_eventually_occupied_seats_model2(orig_seats):
    def _count_neighboors(_seats, row, col):
        directions = [
            (i, j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)
        ]
        n_neighboors = 0
        for (di, dj) in directions:
            i = row
            j = col
            while True:
                i += di
                j += dj
                if i < 0 or j < 0:
                    break
                try:
                    s = _seats[i][j]
                    if s == "#":
                        n_neighboors += 1
                        break
                    elif s == "L":
                        break
                except:
                    break
        return n_neighboors

    def _forward(_seats):
        new_seats = copy.deepcopy(_seats)
        for i in range(len(_seats)):
            for j in range(len(_seats[i])):
                n_neighboors = _count_neighboors(_seats, i, j)
                current = _seats[i][j]
                if current == "L" and n_neighboors == 0:
                    new = "#"
                elif current == "#" and n_neighboors >= 5:
                    new = "L"
                else:
                    continue
                new_seats[i][j] = new
        # print("=== new_seats ===")
        # print("\n".join(["".join(line) for line in new_seats]))
        if new_seats == _seats:
            return sum([r.count("#") for r in _seats])
        else:
            return _forward(new_seats)

    return _forward(orig_seats)


if __name__ == "__main__":
    with open("input") as f:
        seats = [list(line) for line in f.read().splitlines()]
        n1 = count_eventually_occupied_seats_model1(seats)
        print("Model 1 ends with {} seats occupied".format(n1))
        n2 = count_eventually_occupied_seats_model2(seats)
        print("Model 1 ends with {} seats occupied".format(n2))
