with open(f"{__file__.rstrip('code.py')}puzzle_input.txt", mode="r") as file:
    text_input = file.read()

# Part 1 + 2

acc = 0
already_run = []


def parser(text_input):
    commands = [i.split()[0] for i in text_input.split("\n")]
    actions = [int(i.split()[1]) for i in text_input.split("\n")]
    line_counter = [i for i in range(len(commands))]

    dict = {i: [line_counter[i], commands[i], actions[i]]
            for i in line_counter}

    return dict


def run_line(line, dict):
    global acc
    global already_run

    if line[0] not in already_run:
        try:
            already_run.append(line[0])
            if line[1] == "nop":
                run_line(dict[line[0] + 1], dict)
            if line[1] == "acc":
                acc += line[2]
                run_line(dict[line[0] + 1], dict)
            if line[1] == "jmp":
                run_line(dict[line[0] + line[2]], dict)
        except KeyError:
            print(acc)


dict = parser(text_input)

run_line(dict[0], dict)
print(acc)


# Part 2

jmp_nop_list = [i for i in dict.values() if i[1] == "nop" or i[1] == "jmp"]

for i in jmp_nop_list:
    dict = parser(text_input)
    acc = 0
    already_run = []

    if i[1] == "nop":
        dict[i[0]] = [i[0], "jmp", i[2]]
    elif i[1] == "jmp":
        dict[i[0]] = [i[0], "nop", i[2]]

    run_line(dict[0], dict)
