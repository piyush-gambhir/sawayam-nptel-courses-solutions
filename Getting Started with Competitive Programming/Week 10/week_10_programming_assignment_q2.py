n, m = map(int, input().split())
nutritional_values = list(map(int, input().split()))

# Initialize the dp table with a large number and set dp[0] to 0.
dp = [float('inf')] * (m + 1)
dp[0] = 0

for item_value in nutritional_values:
    for i in range(item_value, m + 1):
        dp[i] = min(dp[i], dp[i - item_value] + 1)

if dp[m] == float('inf'):
    print(-1, end="")
else:
    print(dp[m], end="")
