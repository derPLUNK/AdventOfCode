from os import linesep


with open(f"{__file__.rstrip('code.py')}puzzle_input.txt", mode="r") as file:
    text_input = file.read()

lines = [[i[0], int(i[1:])] for i in text_input.split("\n")]


class Position():
    def __init__(self, east=0, north=0):
        self.east = east
        self.north = north
        self.direction = "E"
        self.directions = ["E", "S", "W", "N"]

    def __str__(self):
        return f"{abs(self.east) + abs(self.north)}"

    def turn(self, i):
        index = self.directions.index(
            self.direction)+(int(i[1]/90)*{"R": 1, "L": -1}[i[0]])

        if index >= len(self.directions):
            index -= 4

        self.direction = self.directions[index]

    def move(self, i):
        counters = [self.east, self.north]

        if i[0] == "F":
            self.move([self.direction, i[1]])
        else:
            distance = i[1]*{"E": 1, "N": 1, "S": -1, "W": -1}[i[0]]
            if i[0] in "EW":
                self.east += distance
            else:
                self.north += distance


part1 = Position()

for i in lines:
    if i[0] in "RL":
        part1.turn(i)
    else:
        part1.move(i)


print(part1)
