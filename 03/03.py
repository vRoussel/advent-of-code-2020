#!/usr/bin/python3

def count_trees_with_slope(in_map, dx, dy):
    width = len(in_map[0])
    height = len(in_map)

    x = 0
    y = 0

    n_trees = 0
    while y < height:
        if in_map[y][x] == '#':
            n_trees += 1
        x = (x + dx) % width
        y += dy
    return n_trees

if __name__ == '__main__':
    with open('input') as f:
        in_map = f.read().splitlines()
        total = 1
        for dx,dy in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
            n_trees = count_trees_with_slope(in_map, dx, dy)
            print('{} trees with slope [{},{}]'.format(n_trees, dx, dy))
            total *= n_trees
        print(total)

