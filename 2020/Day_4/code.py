import re

with open(f"{__file__.rstrip('code.py')}puzzle_input.txt", mode="r") as file:
    text_input = file.read()


def list_passports(text):
    text = [[i] for i in text.split("\n\n")]

    return [re.split("[ \n-]", i[0]) for i in text]


def conv_dict(passports):
    return [{x.split(":")[0]: x.split(":")[1] for x in i} for i in passports]


def validate_values(passport):

    for i in [[1920, 2002, "byr"], [2010, 2020, "iyr"], [2020, 2030, "eyr"]]:
        if not i[0] <= int(passport[i[2]]) <= i[1]:
            return False

    height = int(passport["hgt"][:-2])
    unit = passport["hgt"][-2:]

    if unit == "cm":
        if not 150 <= height <= 193:
            return False

    if unit == "in":
        if not 59 <= height <= 76:
            return False

    if not unit in ["in", "cm"]:
        return False

    if passport["hcl"][0] == "#":
        if len(passport["hcl"][1:]) == 6:
            for i in passport["hcl"][1:]:
                if not i in "0123456789abcdef":
                    return False
        else:
            return False
    else:
        return False

    if not passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    if not passport["pid"][0] == 0 and not len(passport["pid"]) == 9:
        return False

    return True


def total_valid_passports(passport_dict):
    total = 0
    total_value_valid = 0

    for i in passport_dict:
        keys = [k for k in i.keys()]
        values = [v for v in i.values()]

        keys.sort()

        try:
            keys.remove("cid")
        except:
            pass

        if keys == ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']:
            if validate_values(i):
                total_value_valid += 1
            total += 1

    return total, total_value_valid


passports = list_passports(text_input)
passports = conv_dict(passports)


print(total_valid_passports(passports)[0])
print(total_valid_passports(passports)[1])
