from copy import deepcopy
from io import SEEK_CUR

with open(f"{__file__.rstrip('code.py')}puzzle_input.txt", mode="r") as file:
    text_input = file.read()


def pretty_print(seat_matrix):
    for row in range(len(seat_matrix)):
        for col in range(len(seat_matrix[0])):
            print(f"{seat_matrix[row][col]}", end="")
        print()


def seats_seen_part1(row, col, initial_matrix, part_number):
    if part_number == 1:
        seats = []

        for i in [-1, 0, 1]:
            for x in [-1, 0, 1]:
                if 0 <= row + i < len(initial_matrix) and 0 <= col + x < len(initial_matrix[0]):
                    seats.append(initial_matrix[row+i][col+x])

        seats[seats.index(initial_matrix[row][col])] = 0

        return seats

    elif part_number == 2:
        seats = []
        for i in range(1, col+1):
            if 0 <= col-i < len(initial_matrix[0]):
                if initial_matrix[row][col-i] in "#L":
                    seats.append(initial_matrix[row][col-i])
                    break
        for i in range(col+1, len(initial_matrix[0])):
            if 0 <= i < len(initial_matrix[0]):
                if initial_matrix[row][i] in "#L":
                    seats.append(initial_matrix[row][i])
                    break
        for i in range(1, row+1):
            if 0 <= row - i < len(initial_matrix):
                if initial_matrix[row-i][col] in "#L":
                    seats.append(initial_matrix[row-i][col])
                    break
        for i in range(row+1, len(initial_matrix)):
            if 0 <= i < len(initial_matrix):
                if initial_matrix[i][col] in "#L":
                    seats.append(initial_matrix[i][col])
                    break

        for i in range(1, col+1):
            if 0 <= row-i < len(initial_matrix) and 0 <= col-i < len(initial_matrix[0]):
                if initial_matrix[row-i][col-i] in "#L":
                    seats.append(initial_matrix[row-i][col-i])
                    break
        for i in range(1, col+1):
            if 0 <= row+i < len(initial_matrix) and 0 <= col-i < len(initial_matrix[0]):
                if initial_matrix[row+i][col-i] in "#L":
                    seats.append(initial_matrix[row+i][col-i])
                    break
        for i in range(1, len(initial_matrix[0])-col):
            if 0 <= row-i < len(initial_matrix) and 0 <= col+i < len(initial_matrix[0]):
                if initial_matrix[row-i][col+i] in "#L":
                    seats.append(initial_matrix[row-i][col+i])
                    break
        for i in range(1, len(initial_matrix[0])-col):
            if 0 <= row+i < len(initial_matrix) and 0 <= col+i < len(initial_matrix[0]):
                if initial_matrix[row+i][col+i] in "#L":
                    seats.append(initial_matrix[row+i][col+i])
                    break
        # if initial_matrix[row][col] in "#L":
        #     print("".join(initial_matrix[row]),
        #           initial_matrix[row][col], row, col, seats, seats.count("#"))
        return seats


def neighbours(row, col, initial_matrix, new_matrix, part_number):
    seats = seats_seen_part1(row, col, initial_matrix, part_number)

    if initial_matrix[row][col] == "L" and "#" not in seats and initial_matrix[row][col] != ".":
        new_matrix[row][col] = "#"
    if part_number == 1:
        if initial_matrix[row][col] == "#" and seats.count("#") >= 4:
            new_matrix[row][col] = "L"
    if part_number == 2:
        if initial_matrix[row][col] == "#" and seats.count("#") > 4:
            new_matrix[row][col] = "L"

    return new_matrix


def run_part(part_number, seat_matrix):
    initial_matrix = deepcopy(seat_matrix)
    new_matrix = deepcopy(seat_matrix)

    for row in range(len(seat_matrix)):
        for col in range(len(seat_matrix[0])):
            matrix = neighbours(
                row, col, initial_matrix, new_matrix, part_number)

    return matrix


def run(part_number):
    seat_matrix = [list(i) for i in text_input.split("\n")]

    while True:
        seat_matrix = run_part(part_number, seat_matrix)
        if seat_matrix == run_part(part_number, seat_matrix):
            total = 0
            for i in seat_matrix:
                total += i.count("#")
            print(total)
            break


run(1)
run(2)
