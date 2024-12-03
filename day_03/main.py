# PART 1

# import re
#
# with open("data.txt") as data_file:
#     content = data_file.read()
#
# pattern = (r"mul\((\d+)[,](\d+)[\)]")
# list_of_tuples = re.findall(pattern, content)
#
# total = 0
#
# for tuple in list_of_tuples:
#     total += int(tuple[0]) * int(tuple[1])
#
# print(f"{total}")

#  PART 2

import re

with open("data.txt") as data_file:
    content = data_file.read()

dont_do_pattern = (r"(don't\(\)|do\(\))|mul\((\d+)[,](\d+)[\)]")

list_of_tuples = re.findall(dont_do_pattern, content)
total = 0
action = True

for tuple in list_of_tuples:

    if tuple[0] == "don't()":
        action = False

    elif tuple[0] == "do()":
        action = True

    if action:
        if tuple[1] != '':
            total += int(tuple[1]) * int(tuple[2])

print(f"{total}")

