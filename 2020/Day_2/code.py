with open(f"{__file__.rstrip('code.py')}puzzle_input.txt", mode="r") as file:
    text_input = file.read()

lines = text_input.split("\n")

min = []
max = []
letter = []
password = []

for i in lines:
    min.append(int(i.split("-")[0]))
    max.append(int(i.split("-")[1].split(" ")[0]))
    letter.append(i.split(":")[0][-1])
    password.append(i.split(": ")[1])

# Part 1
total_valid = 0

for i in range(len(lines)):
    if min[i] <= password[i].count(letter[i]) <= max[i]:
        total_valid += 1

print(total_valid)

# Part 2
total_valid = 0

for i in range(len(lines)):
    if password[i][min[i]-1] == letter[i] or password[i][max[i]-1] == letter[i]:
        total_valid += 1
    if password[i][min[i]-1] == letter[i] and password[i][max[i]-1] == letter[i]:
        total_valid -= 1

print(total_valid)
