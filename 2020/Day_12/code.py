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
        if i[0] == "F":
            self.move([self.direction, i[1]])
        else:
            distance = i[1]*{"E": 1, "N": 1, "S": -1, "W": -1}[i[0]]
            if i[0] in "EW":
                self.east += distance
            else:
                self.north += distance

    def move_ship(self, waypoint_position, i):
        self.east += waypoint_position[0] * i[1]
        self.north += waypoint_position[1] * i[1]

    def turn_waypoint(self, i):
        if i[0] == "R" and i[1] > 0:
            current_position = self.current_position()
            self.east = current_position[1]
            self.north = -current_position[0]
            self.turn_waypoint([i[0], i[1] - 90])

        if i[0] == "L" and i[1] > 0:
            current_position = self.current_position()
            self.east = -current_position[1]
            self.north = current_position[0]
            self.turn_waypoint([i[0], i[1] - 90])

    def current_position(self):
        return [self.east, self.north]


ship_part_1 = Position()
waypoint_part_2 = Position(10, 1)
ship_part_2 = Position()

# Part 1
for i in lines:
    if i[0] in "RL":
        ship_part_1.turn(i)
    else:
        ship_part_1.move(i)

# Part 2
for i in lines:
    if i[0] == "F":
        ship_part_2.move_ship(waypoint_part_2.current_position(), i)
    if i[0] in "ESWN":
        waypoint_part_2.move(i)
    if i[0] in "LR":
        waypoint_part_2.turn_waypoint(i)


print(ship_part_1)
print(ship_part_2)
