# PART 1

# with open("data.txt") as data_file:
#     content = data_file.read()
#
# rule_list, data_content = content.split("\n\n")
#
# rules_list = [rule.split("|") for rule in rule_list.split("\n")]
# data_list = [data.split(",") for data in data_content.split("\n")]
#
#
# def find_relevant_rules(data):
#     relevant_rule_list = []
#     counter = 0
#
#     for rule in rules_list:
#
#         if rule[0] in data and rule[1] in data:
#
#             if data.index(rule[0]) < data.index(rule[1]):
#
#                 counter += 1
#                 # print(f"{rule}: {data}")
#
#             relevant_rule_list.append(rule)
#
#     return relevant_rule_list, counter
#
#
# compliancy = 0
# running_total = 0
#
# for line in data_list:
#     list, counter = find_relevant_rules(line)
#
#     if counter == len(list):
#         index = len(line) // 2
#         running_total += int(line[index])
#
# print(running_total)

# PART 2

with open("data.txt") as data_file:
    content = data_file.read()

rule_list, data_content = content.split("\n\n")

rules_list = [rule.split("|") for rule in rule_list.split("\n")]
data_list = [data.split(",") for data in data_content.split("\n")]


def find_relevant_rules(data):
    relevant_rule_list = []
    counter = 0

    for rule in rules_list:

        if rule[0] in data and rule[1] in data:

            if data.index(rule[0]) < data.index(rule[1]):

                counter += 1

            relevant_rule_list.append(rule)

    return relevant_rule_list, counter


lines_to_sort = []


for line in data_list:
    list, counter = find_relevant_rules(line)

    if counter != len(list):
        lines_to_sort.append(line)


def sort_lines_and_check(data):

    fully_compliant = False

    while not fully_compliant:

        number_of_swaps = 0
        swap_not_necessary = 0

        relevant_rule_list = set()

        for rule in rules_list:

            if rule[0] in data and rule[1] in data:

                relevant_rule_list.add((rule[0], rule[1]))

                if data.index(rule[0]) > data.index(rule[1]):

                    data[data.index(rule[0])], data[data.index(rule[1])] = data[data.index(rule[1])], data[data.index(rule[0])]

                    number_of_swaps += 1

                else:
                    swap_not_necessary += 1

        if swap_not_necessary == len(relevant_rule_list):

            fully_compliant = True

    return relevant_rule_list, data


running_total = 0

for line in lines_to_sort:

    relevant_rules, new_line = sort_lines_and_check(line)

    index = len(new_line) // 2
    running_total += int(new_line[index])

print(running_total)

