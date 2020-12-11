from copy import deepcopy

with open(f"{__file__.rstrip('code.py')}puzzle_input.txt", mode="r") as file:
    text_input = file.read()


def pretty_print(seat_matrix):
    for row in range(len(seat_matrix)):
        for col in range(len(seat_matrix[0])):
            print(f"{seat_matrix[row][col]}", end="")
        print()


def neighbours(row, col, initial_matrix, new_matrix):
    seats = []

    for i in [-1, 0, 1]:
        for x in [-1, 0, 1]:
            if 0 <= row + i < len(initial_matrix) and 0 <= col + x < len(initial_matrix[0]):
                seats.append(initial_matrix[row+i][col+x])

    seats[seats.index(initial_matrix[row][col])] = 0

    if initial_matrix[row][col] == "L" and "#" not in seats and initial_matrix[row][col] != ".":
        new_matrix[row][col] = "#"
    if initial_matrix[row][col] == "#" and seats.count("#") >= 4:
        new_matrix[row][col] = "L"

    return new_matrix


seat_matrix = [list(i) for i in text_input.split("\n")]


def run_part1(seat_matrix=seat_matrix):
    initial_matrix = deepcopy(seat_matrix)
    new_matrix = deepcopy(seat_matrix)

    for row in range(len(seat_matrix)):
        for col in range(len(seat_matrix[0])):
            new_matrix = neighbours(row, col, initial_matrix, new_matrix)

    return new_matrix


while True:
    seat_matrix = run_part1(seat_matrix)
    if seat_matrix == run_part1(seat_matrix):
        total = 0
        for i in seat_matrix:
            total += i.count("#")
        print(total)
        break
