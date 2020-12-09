with open(f"{__file__.rstrip('code.py')}puzzle_input.txt", mode="r") as file:
    text_input = file.read()


def determine_seat(instruction, max, min=0):
    for i in instruction:
        half = (max - min) // 2 + min

        if i == "B" or i == "R":
            min = half + 1
        if i == "F" or i == "L":
            max = half

    return min


ticket_list = [i for i in text_input.split("\n")]


row = [determine_seat(i, 127) for i in [i[:7] for i in ticket_list]]
column = [determine_seat(i, 7) for i in [i[7:] for i in ticket_list]]

id = [row[i]*8 + column[i] for i in range(len(row))]

id.sort()


print(max(id))
print([i for i in range(min(id), max(id)) if i not in id])
