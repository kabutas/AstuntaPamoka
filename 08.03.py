import random

dictNums = {}

# print(type(dictNums))

for i in range(10):
    dictNums[i+1] = random.randint(1, 100)

print(dictNums)

