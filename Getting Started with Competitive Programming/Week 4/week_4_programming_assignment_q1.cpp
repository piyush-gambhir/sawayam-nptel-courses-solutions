#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin >> n;
    unordered_map<int, int> m;
    int x = n;
    vector<int> c(1e6 + 1, 0);
    vector<int> d(1e6 + 1, 0);
    while (x--)
    {
        int a, b;
        cin >> a >> b;
        m[a] = b;
        c[a] = 1;
        d[b] = 1;
    }
    int i = 3;
    vector<int> ans(n, 0);
    ans[1] = m[0];
    while (i < n)
    {
        ans[i] = m[ans[i - 2]];
        i += 2;
    }
    int temp;
    for (int i = 1; i < 1e6; i++)
    {
        if (c[i] && d[i] == 0)
        {
            temp = i;
            break;
        }
    }
    ans[0] = temp;
    i = 2;
    while (i < n)
    {
        ans[i] = m[ans[i - 2]];
        i += 2;
    }
    for (auto i : ans)
        cout << i << " ";
    return 0;
}