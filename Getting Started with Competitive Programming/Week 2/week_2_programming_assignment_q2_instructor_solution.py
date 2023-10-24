count, sortNum = [
    int(value) for value in input().split()]

numList = [int(value) for value in input().split()]

sortedList = []
prev = 0
for i in range(0, min(count, count+sortNum), sortNum):
    sortedList += sorted(numList[prev:i])
    prev = i
if prev < count:
    sortedList += sorted(numList[prev:])

str_out = ""
for i in range(count):
    str_out += str(sortedList[i]) + " "

print(str_out)
