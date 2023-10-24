#include <bits/stdc++.h>
using namespace std;

int dp[10001];

int loop(int m, int cost, int mem)
{
    if (m == 0)
        return cost;
    cost = dp[m - 1] + 1;
    for (int i = m - 2; i > 0; i--)
    {
        int tempcost = cost;
        int j = m;
        if (dp[i] + 6 < tempcost)
        {
            mem = i;
            tempcost = dp[i] + 6;
            j = j - 2 * mem;
            if (j < 0)
                continue;
            tempcost += 2 * (j / mem) + (j % mem);
        }
        cost = min(cost, tempcost);
    }
    return cost;
}
int getMin(int n)
{
    if (dp[n])
        return dp[n];
    for (int i = 2; i <= n; i++)
    {
        int x = loop(i, 0, 0);
        dp[i] = x;
    }
    return dp[n];
}
int main()
{
    dp[1] = 1;
    int t;
    cin >> t;
    while (t--)
    {
        int x;
        cin >> x;
        cout << getMin(x) << endl;
    }
}