#!/usr/bin/python3

import math
from collections import namedtuple


def lcm(a, b):
    a = int(a)
    b = int(b)
    return int(abs(a * b) / math.gcd(a, b))


Bus = namedtuple("Bus", ["pos", "freq"])

if __name__ == "__main__":
    with open("input") as f:
        min_departure_ts = int(f.readline().rstrip())
        raw_buses = f.readline().rstrip()
        buses = [
            Bus(i, int(freq))
            for i, freq in enumerate(raw_buses.split(","))
            if freq.isnumeric()
        ]

        # Part 1
        part1_ts = math.inf
        earlier_bus_id = None
        for bus in buses:
            next_departure_ts = math.ceil(min_departure_ts / bus.freq) * bus.freq
            if next_departure_ts < part1_ts:
                part1_ts = next_departure_ts
                earliest_bus_id = bus.freq
        waiting_time = part1_ts - min_departure_ts
        print(
            "First departure before {} is bus {} after {}min (answer: {})".format(
                min_departure_ts,
                earliest_bus_id,
                waiting_time,
                waiting_time * earliest_bus_id,
            )
        )

        # Part 2
        step = buses[0].freq
        part2_ts = buses[0].freq + buses[0].pos
        for bus in buses[1:]:
            while True:
                if (part2_ts + bus.pos) % bus.freq == 0:
                    step = lcm(step, bus.freq)
                    break
                part2_ts += step
        print("First syncronized departure is at {}".format(part2_ts))
