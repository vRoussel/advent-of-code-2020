#!/usr/bin/python3

from enum import Enum
from dataclasses import dataclass


class Direction(Enum):
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"
    LEFT = "L"
    RIGHT = "R"
    FORWARD = "F"

    def isCardinal(self):
        return self.value in "NSEW"

    def isRotational(self):
        return self.value in "LR"


@dataclass
class Coord:
    x: int
    y: int

    def moveTowards(self, other, n):
        self.x += other.x * n
        self.y += other.y * n

    def rotate(self, angle):
        normalized_angle = angle % 360
        if normalized_angle == 0:
            pass
        elif normalized_angle == 90:
            self.x, self.y = self.y, -self.x
        elif normalized_angle == 180:
            self.x, self.y = -self.x, -self.y
        elif normalized_angle == 270:
            self.x, self.y = -self.y, self.x
        else:
            raise Exception("Invalid angle of rotation: ", angle)

    @classmethod
    def fromDirection(cls, d):
        if d == Direction.NORTH:
            return cls(0, 1)
        elif d == Direction.SOUTH:
            return cls(0, -1)
        elif d == Direction.EAST:
            return cls(1, 0)
        elif d == Direction.WEST:
            return cls(-1, 0)
        else:
            raise Exception(
                "Direction to coord conversion is only possible with cardinal direction, and not %s",
                d,
            )


class Ship:
    def __init__(self, wp):
        self.position = Coord(0, 0)
        self.waypoint = wp

    def move(self, d, n):
        if d == Direction.FORWARD:
            self.position.moveTowards(self.waypoint, n)
        elif d.isCardinal():
            self.position.moveTowards(Coord.fromDirection(d), n)
        elif d.isRotational():
            self._rotate(d, n)

    def moveWaypoint(self, d, n):
        if d.isCardinal():
            self.waypoint.moveTowards(Coord.fromDirection(d), n)
        elif d.isRotational():
            self._rotate(d, n)
        else:
            raise Exception("Cannot move waypoint in the direction: %s", d)

    def _rotate(self, d, angle):
        if d == Direction.RIGHT:
            k = 1
        else:
            k = -1
        signed_angle = k * angle
        self.waypoint.rotate(signed_angle)

    def man_distance(self):
        return abs(self.position.x) + abs(self.position.y)


if __name__ == "__main__":
    direction = Direction.EAST
    with open("input") as f:
        ship1 = Ship(Coord.fromDirection(Direction.EAST))
        ship2 = Ship(Coord(10, 1))
        for line in f:
            line = line.rstrip()
            _dir, _num = Direction(line[0]), int(line[1:])
            ship1.move(_dir, _num)
            if _dir == Direction.FORWARD:
                ship2.move(_dir, _num)
            else:
                ship2.moveWaypoint(_dir, _num)
        print("Manhattan distance for ship1: {}".format(ship1.man_distance()))
        print("Manhattan distance for ship2: {}".format(ship2.man_distance()))
