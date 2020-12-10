from collections import Counter

with open(f"{__file__.rstrip('code.py')}puzzle_input.txt", mode="r") as file:
    text_input = file.read()

jolts = sorted([int(i) for i in text_input.split("\n")]+[0])
jolts.append(max(jolts)+3)
jolt_1, jolt_3 = 0, 0


def get_1_3_jolts(number, jolts=jolts):
    global jolt_1
    global jolt_3
    index = jolts.index(number)
    i = jolts[index+1:index+2][0]

    if i - number == 1:
        jolt_1 += 1
    elif i - number == 3:
        jolt_3 += 1


for i in jolts[:-1]:
    get_1_3_jolts(i)

print(jolt_1 * jolt_3)


# not my own solution and I don't understand it
c = Counter({0: 1})
for x in jolts:
    c[x+1] += c[x]
    c[x+2] += c[x]
    c[x+3] += c[x]

print(c[max(jolts) + 3])
