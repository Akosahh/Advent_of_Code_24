with open("data.txt") as data:
    content = data.readlines()

data_list = []

for line in content:
    data_list.append(line.strip("\n"))

#
# def find_horizontal(crossword):
#     counter = 0
#
#     for i in range(len(crossword)):
#         for j in range(len(crossword[0]) - 3):
#
#             current = crossword[i][j]
#             second = crossword[i][j+1]
#             third = crossword[i][j+2]
#             fourth = crossword[i][j+3]
#
#             if f"{current}{second}{third}{fourth}" == "XMAS" or f"{current}{second}{third}{fourth}" == "SAMX":
#                 counter += 1
#
#     return counter
#
#
# def find_vertical(crossword):
#     counter = 0
#
#     for i in range(len(crossword) - 3):
#         for j in range(len(crossword[0])):
#
#             current = crossword[i][j]
#             second = crossword[i + 1][j]
#             third = crossword[i + 2][j]
#             fourth = crossword[i + 3][j]
#
#             if f"{current}{second}{third}{fourth}" == "XMAS" or f"{current}{second}{third}{fourth}" == "SAMX":
#                 counter += 1
#
#     return counter
#
#
# def find_l_r_diagonal(crossword):
#     counter = 0
#
#     for i in range(len(crossword) - 3):
#         for j in range(len(crossword[0]) - 3):
#
#             current = crossword[i][j]
#             second = crossword[i + 1][j + 1]
#             third = crossword[i + 2][j + 2]
#             fourth = crossword[i + 3][j + 3]
#
#             if f"{current}{second}{third}{fourth}" == "XMAS" or f"{current}{second}{third}{fourth}" == "SAMX":
#                 counter += 1
#
#     return counter
#
#
# def find_r_l_diagonal(crossword):
#     counter = 0
#
#     for i in range(len(crossword) - 3):
#         for j in range(3, len(crossword[0])):
#
#             current = crossword[i][j]
#             second = crossword[i + 1][j - 1]
#             third = crossword[i + 2][j - 2]
#             fourth = crossword[i + 3][j - 3]
#
#             if f"{current}{second}{third}{fourth}" == "XMAS" or f"{current}{second}{third}{fourth}" == "SAMX":
#                 counter += 1
#
#     return counter
#
#
# def search_crossword(crossword):
#     total = \
#         find_l_r_diagonal(crossword) + \
#         find_r_l_diagonal(crossword) + \
#         find_vertical(crossword) + \
#         find_horizontal(crossword)
#
#     return total
#
#
# print(search_crossword(data_list))

# 00 01 02 03 NO A
# 10 11 12 13
# 20 21 22 23
# 30 31 32 33


def find_a(crossword):
    counter = 0

    print(len(crossword))
    print(len(crossword[0]))

    for i in range(len(crossword)):
        for j in range(len(crossword[0])):

            if crossword[i][j] == "A" and len(crossword) - 1 > i > 0 and len(crossword[0]) - 1 > j > 0:

                centre_A = crossword[i][j]
                top_left = crossword[i - 1][j - 1]
                top_right = crossword[i - 1][j + 1]
                bottom_left = crossword[i + 1][j - 1]
                bottom_right = crossword[i + 1][j + 1]

                if f"{top_left}{centre_A}{bottom_right}" == "MAS" or f"{top_left}{centre_A}{bottom_right}" == "SAM":
                    if f"{top_right}{centre_A}{bottom_left}" == "MAS" or f"{top_right}{centre_A}{bottom_left}" == "SAM":
                        counter += 1

    return counter


total = find_a(data_list)
print(total)
