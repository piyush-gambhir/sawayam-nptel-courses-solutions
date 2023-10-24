#include <bits/stdc++.h>
#define ll long long
using namespace std;

ll dfs(int n, int m, vector<vector<ll>> &a, int i, int j)
{
    if (i < 0 || j < 0)
        return 0;
    if (i == n || j == m)
        return 0;
    if (a[i][j] == 0)
        return 0;
    ll k = a[i][j];
    a[i][j] = 0;
    return k + dfs(n, m, a, i + 1, j) + dfs(n, m, a, i, j + 1) + dfs(n, m, a, i - 1, j) + dfs(n, m, a, i, j - 1);
}
int main()
{
    int n, m;
    cin >> n >> m;
    ll ans = 0;
    vector<vector<ll>> a(n, vector<ll>(m, 0));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> a[i][j];

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
        {
            if (a[i][j])
            {
                ll sum = dfs(n, m, a, i, j);
                ans = max(sum, ans);
            }
        }
    cout << ans;
    return 0;
}
