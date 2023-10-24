from bisect import bisect_right

n = int(input())
granites = list(map(int, input().split()))

gopuram_tops = []

for granite in granites:
    idx = bisect_right(gopuram_tops, granite)

    if idx < len(gopuram_tops):
        gopuram_tops[idx] = granite
    else:
        gopuram_tops.append(granite)

print(len(gopuram_tops), end='')
