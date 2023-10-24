def min_operations_to_power_of_two(nums):
    powers_of_2 = [str(2**i) for i in range(18)]
    results = []
    for num in nums:
        num = str(num)
        min_ops = float('inf')
        for power in powers_of_2:
            ops = 0
            j = 0
            for i in range(len(num)):
                if j < len(power) and num[i] == power[j]:
                    j += 1
            ops = len(num) - j + len(power) - j
            min_ops = min(min_ops, ops)
        results.append(min_ops)
    return results


t = int(input())
nums = [int(input()) for _ in range(t)]

for i, result in enumerate(min_operations_to_power_of_two(nums)):
    if i == t - 1:
        print(result, end="")
    else:
        print(result)
