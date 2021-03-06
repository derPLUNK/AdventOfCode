with open(f"{__file__.rstrip('code.py')}puzzle_input.txt", mode="r") as file:
    text_input = file.read()

matrix = [list(i) for i in text_input.split("\n")]


def num_trees(right, down):
    total_trees = 0
    pointer = 0

    for i in range(0, len(matrix)-down, down):
        for x in range(right):
            if pointer == len(matrix[0])-1:
                pointer = -1
            pointer += 1

        if matrix[i+down][pointer] == "#":
            total_trees += 1

    return total_trees


total = 1

for i in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:
    x = num_trees(i[0], i[1])
    total *= x

print(num_trees(3, 1))
print(total)
