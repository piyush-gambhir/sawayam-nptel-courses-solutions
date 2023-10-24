def partition_and_sort(m, b, numbers):
    partitions = [numbers[i:i+b] for i in range(0, m, b)]
    sorted_partitions = [sorted(part) for part in partitions]
    result = [num for part in sorted_partitions for num in part]
    return result


m, b = map(int, input().split())
numbers = list(map(int, input().split()))

resulting_list = partition_and_sort(m, b, numbers)
print(*resulting_list, end='')
