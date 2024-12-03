
# PART 1
# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.

# with open("data.txt") as data:
#     content = data.readlines()
#
# contentList = [[int(num) for num in item.strip("\n").replace(" ", ", ").split(", ")] for item in content]
#
# # test = [7, 6, 4, 2, 1]
# # decreasingCount = 0
# # increasingCount = 0
# # strikes = 0
#
# #
# # for i in range(len(test) - 1):
# #
# #     currentNum = test[i]
# #     nextNum = test[i + 1]
# #     print(currentNum, " ", nextNum)
# #
# #     if currentNum > nextNum:
# #         decreasingCount += 1
# #
# #         if (currentNum - nextNum) > 3:
# #             strikes += 1
# #
# # if decreasingCount != 0 and increasingCount != 0:
# #     strikes += 1
# #
# # if strikes == 0:
# #     safe = True
# # else:
# #     safe = False
# #
# #
# # print(safe)
# # print(increasingCount)
# # print(decreasingCount)
# # print(strikes)
#
# totalSafe = 0
#
# for item in contentList:
#
#     safe = True
#
#     decreasingCount = 0
#     increasingCount = 0
#
#     for i in range(len(item) - 1):
#
#         currentNum = item[i]
#         nextNum = item[i+1]
#
#         if currentNum > nextNum:
#             decreasingCount += 1
#
#             if currentNum - nextNum > 3:
#                 safe = False
#
#         elif currentNum < nextNum:
#             increasingCount += 1
#
#             if nextNum - currentNum > 3:
#                 safe = False
#
#         else:
#             safe = False
#
#         if increasingCount != 0 and decreasingCount != 0:
#             safe = False
#
#     if safe:
#         totalSafe += 1
#
# print(totalSafe)


#  PART 2

with open("data.txt") as data:
    content = data.readlines()

contentList = [[int(num) for num in item.strip("\n").replace(" ", ", ").split(", ")] for item in content]

totalSafe = 0


def safe_checker(item):

    safe = True

    decreasingCount = 0
    increasingCount = 0

    for i in range(len(item) - 1):

        currentNum = item[i]
        nextNum = item[i+1]

        if currentNum > nextNum:
            decreasingCount += 1

            if currentNum - nextNum > 3:
                safe = False

        elif currentNum < nextNum:
            increasingCount += 1

            if nextNum - currentNum > 3:
                safe = False

        else:
            safe = False

        if increasingCount != 0 and decreasingCount != 0:
            safe = False

    return safe


safeCount = 0

for item in contentList:
    safe = safe_checker(item)

    j = 0

    while j != len(item) and not safe:

        testCopy = item.copy()
        testCopy.pop(j)
        safe = safe_checker(testCopy)

        j += 1

    if safe:
        safeCount += 1

print(safeCount)





