with open(f"{__file__.rstrip('code.py')}puzzle_input.txt", mode="r") as file:
    text_input = file.read()


numbers = [int(i) for i in text_input.split("\n")]


def get_previous(numbers, amount, number):
    index = numbers.index(number)

    max = index
    min = index - amount

    return numbers[min:max]


def is_sum_of_previous(previous_numbers, number):
    if previous_numbers:
        for i in previous_numbers:
            for x in previous_numbers:
                if i != x and i + x == number:
                    return True
    else:
        return True


def get_list_adding_to_magic(numbers, magic):
    for i in numbers:
        index = numbers.index(i)
        contiguous_list = []
        while sum(contiguous_list) < magic:
            contiguous_list.append(numbers[index])
            index += 1

        if sum(contiguous_list) == magic:
            return min(contiguous_list) + max(contiguous_list)


for i in numbers:
    previous_numbers = get_previous(numbers, 25, i)

    if is_sum_of_previous(previous_numbers, i) == None:
        print(i)
        magic = i

print(get_list_adding_to_magic(numbers, magic))
