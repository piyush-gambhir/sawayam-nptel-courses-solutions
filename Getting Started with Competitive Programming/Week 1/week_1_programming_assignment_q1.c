#include <stdio.h>
#include <stdlib.h>

typedef long long ll;

int main()
{
    int t;
    scanf("%d", &t);
    while (t--)
    {
        ll n, m;
        scanf("%lld %lld", &n, &m);
        ll vk[n], lm[m];
        for (int i = 0; i < n; i++)
        {
            scanf("%lld", &vk[i]);
        }
        for (int i = 0; i < m; i++)
        {
            scanf("%lld", &lm[i]);
        }
        int i = 0, j = 0;
        while (i < n && j < m)
        {
            if (vk[i] == lm[j])
            {
                vk[i] = 0;
                lm[j] = 0;
                i++;
                j++;
            }
            else if (vk[i] > lm[j])
            {
                vk[i] -= lm[j];
                j++;
            }
            else
            {
                lm[j] -= vk[i];
                i++;
            }
        }
        if (i == n && j == m)
        {
            printf("Draw\n");
        }
        else if (i == n)
        {
            ll cost = 0;
            for (int k = j; k < m; k++)
            {
                cost += lm[k];
                if (cost > 0)
                {
                    break;
                }
            }
            if (cost > 0)
            {
                printf("Duryodhana\n");
            }
            else
            {
                printf("Draw\n");
            }
        }
        else
        {
            ll cost = 0;
            for (int k = i; k < n; k++)
            {
                cost += vk[k];
                if (cost > 0)
                {
                    break;
                }
            }
            if (cost > 0)
            {
                printf("Yudhisthira\n");
            }
            else
            {
                printf("Draw\n");
            }
        }
    }
    return 0;
}
