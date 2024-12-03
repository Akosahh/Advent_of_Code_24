# PART 1

with open("data.txt") as data:
    content = data.read().replace("   ", ", ").replace("\n", ", ").split(", ")

listA = []
listB = []

for i in range(0, len(content)):
    if i % 2 == 0:
        listA.append(int(content[i]))
    else:
        listB.append(int(content[i]))

sortedListA = sorted(listA)
sortedListB = sorted(listB)

total = 0

for i in range(0, len(sortedListA)):
    if sortedListA[i] >= sortedListB[i]:
        total += sortedListA[i] - sortedListB[i]
    else:
        total += sortedListB[i] - sortedListA[i]

print(total)

#  PART 2

with open("data.txt") as data:
    content = data.read().replace("   ", ", ").replace("\n", ", ").split(", ")

contentList = [int(item) for item in content]

listA = []
listB = []

for i in range(0, len(contentList)):
    if i % 2 == 0:
        listA.append((contentList[i]))
    else:
        listB.append((contentList[i]))

sortedListA = sorted(listA)
sortedListB = sorted(listB)

total = 0

for i in range(len(sortedListA)):

    counter = 0

    for j in range(len(sortedListB)):

        if sortedListA[i] == sortedListB[j]:

            counter += 1

    total += sortedListA[i] * counter



print(total)