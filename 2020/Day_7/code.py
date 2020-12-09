with open(f"{__file__.rstrip('code.py')}puzzle_input.txt", mode="r") as file:
    text_input = file.read()

containers = [i.split(" contain")[0].rstrip("s")
              for i in text_input.split("\n")]
contents = [i.split(" contain")[1] for i in text_input.split("\n")]


def split_words(contents):
    output = []

    for i in contents.split(", "):
        if i != " no other bags.":
            count, name1, name2, bag = i.split()
            output.append([int(count), name1 + " " +
                           name2 + " " + bag.rstrip("s.")])

    return output


def bag_contains(bag, rule_dict):
    for i in rule_dict[bag]:
        if i[1] == "shiny gold bag" or bag_contains(i[1], rule_dict):
            return True
    return False


def num_bags(bag, rule_dict):
    return sum(i[0] * (1 + num_bags(i[1], rule_dict)) for i in rule_dict[bag])


rule_dict = dict(zip(containers, [split_words(i) for i in contents]))

total_golds = 0
for i in rule_dict.keys():
    if bag_contains(i, rule_dict):
        total_golds += 1

print(total_golds)
print(num_bags("shiny gold bag", rule_dict))
