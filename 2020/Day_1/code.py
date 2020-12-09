with open(f"{__file__.rstrip('code.py')}puzzle_input.txt", mode="r") as file:
    text_input = file.read()

numbers = [int(i) for i in text_input.split("\n")]


def find_two_numbers(numbers=numbers):
    for i in numbers:
        for x in numbers:
            if i + x == 2020:
                return i*x


def find_three_numbers(numbers=numbers):
    for y in numbers:
        for i in numbers:
            for x in numbers:
                if i + x + y == 2020:
                    return i*x*y


print(find_two_numbers())
print(find_three_numbers())
