#include <bits/stdc++.h>

#define gupt_loopCounter(i, gupt_start, gupt_end) for(int i = gupt_start; i < gupt_end; i++)
#define gupt_longLongInteger long long
#define gupt_constantModulus 1000000007
#define gupt_endLine std::cout << std::endl
using namespace std;

long long gupt_primeFunction(vector<vector<int>> gupt_graph[], bool gupt_isVisited[], int gupt_initialVertex)
{
    gupt_longLongInteger gupt_totalCost = 0;

    set<vector<int>> gupt_priorityQueue;

    for (int i = 0; i < gupt_graph[gupt_initialVertex].size(); i++)
    {
        gupt_priorityQueue.insert({gupt_graph[gupt_initialVertex][i][1], gupt_initialVertex, gupt_graph[gupt_initialVertex][i][0]});
    }

    while (!gupt_priorityQueue.empty())
    {
        auto gupt_value = *(gupt_priorityQueue.begin());

        int gupt_u = gupt_value[1];
        int gupt_v = gupt_value[2];
        int gupt_w = gupt_value[0];

        gupt_priorityQueue.erase(gupt_priorityQueue.begin());

        if (!gupt_isVisited[gupt_u] || !gupt_isVisited[gupt_v])
        {
            if (gupt_isVisited[gupt_u] == false)
            {
                for (int i = 0; i < gupt_graph[gupt_u].size(); i++)
                {
                    gupt_priorityQueue.insert({gupt_graph[gupt_u][i][1], gupt_u, gupt_graph[gupt_u][i][0]});
                }
            }
            gupt_isVisited[gupt_u] = true;

            if (gupt_isVisited[gupt_v] == false)
            {
                for (int i = 0; i < gupt_graph[gupt_v].size(); i++)
                {
                    gupt_priorityQueue.insert({gupt_graph[gupt_v][i][1], gupt_v, gupt_graph[gupt_v][i][0]});
                }
            }
            gupt_isVisited[gupt_v] = true;

            gupt_totalCost += 1LL * gupt_w;
        }
    }
    return gupt_totalCost;
}

int main()
{
    int gupt_vertices, gupt_edges, gupt_multiplier;
    cin >> gupt_vertices >> gupt_edges >> gupt_multiplier;

    vector<vector<int>> gupt_graph[gupt_vertices + 1];

    gupt_loopCounter(i, 0, gupt_edges)
    {
        int gupt_vertexU, gupt_vertexV, gupt_weight;
        cin >> gupt_vertexU >> gupt_vertexV >> gupt_weight;

        gupt_graph[gupt_vertexU].push_back({gupt_vertexV, gupt_weight});
        gupt_graph[gupt_vertexV].push_back({gupt_vertexU, gupt_weight});
    }

    bool gupt_isVisited[gupt_vertices + 1] = {false};

    long long gupt_maximum = gupt_primeFunction(gupt_graph, gupt_isVisited, 1);

    gupt_maximum = 2 * gupt_multiplier * gupt_maximum;

    cout << gupt_maximum;

    return 0;
}