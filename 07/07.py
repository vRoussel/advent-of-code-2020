#!/usr/bin/python3

import re

MY_BAG = "shiny gold"

class Bag:
    def __init__(self, _name):
        self.name = _name
        self.content = []
        self.containers = []

    def __repr__(self):
        return self.name

bags_index = {}

def find_all_containers_of_bag(bag):
    def _find_containers(queue, containers = set()):
        if queue:
            next_bag = queue.pop(0)
            if next_bag not in containers:
                containers.add(next_bag)
                new_containers = [b for (n,b) in next_bag.containers]
                queue.extend(new_containers)
            _find_containers(queue, containers)
        return containers

    first_level_containers = [b for (n,b) in bag.containers]
    return _find_containers(first_level_containers)

def find_number_of_bags_inside(bag):
    def _count_bags_inside(queue):
        count = 0
        for _n, _bag in queue:
            count += _n
            count += _n * _count_bags_inside(_bag.content)
        return count

    return _count_bags_inside(bag.content)

if __name__ == '__main__':
    re_out_bag = re.compile(r'^([\w\s]*?) bag')
    re_in_bag = re.compile(r'(\d+) ([\w\s]*?) bag')
    with open('input') as f:
        for line in f:
            line = line.rstrip()
            try:
                out_bag_name = re_out_bag.search(line).group(1)
                in_bag_names = re_in_bag.findall(line)

                if out_bag_name not in bags_index:
                    bags_index[out_bag_name] = Bag(out_bag_name)
                out_bag = bags_index[out_bag_name]

                for (n, in_bag_name) in in_bag_names:
                    n = int(n)
                    if n == 0:
                        continue
                    if in_bag_name not in bags_index:
                        bags_index[in_bag_name] = Bag(in_bag_name)
                    in_bag = bags_index[in_bag_name]

                    in_bag.containers.append( (n, out_bag) )
                    out_bag.content.append( (n, in_bag) )
            except:
                continue

    my_bag = bags_index[MY_BAG]
    containers = find_all_containers_of_bag(my_bag)
    print("{} containers found for {}".format(len(containers), my_bag))

    n_inside_bags = find_number_of_bags_inside(my_bag)
    print("{} bags in {}".format(n_inside_bags, my_bag))
