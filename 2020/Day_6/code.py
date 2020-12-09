with open(f"{__file__.rstrip('code.py')}puzzle_input.txt", mode="r") as file:
    text_input = file.read()

groups = text_input.split("\n\n")

# part 1
people = [set(x for x in i if x != "\n") for i in groups]

print(sum([len(i) for i in people]))

# part 2
group_len = [len(i.split("\n")) for i in groups]
people = [[x for x in i if x != "\n"] for i in groups]


def same_answers(people, group_len):
    total = 0

    for i in set(people):
        if people.count(i) == group_len:
            total += 1

    return total


print(sum([same_answers(people[i], group_len[i]) for i in range(len(people))]))
