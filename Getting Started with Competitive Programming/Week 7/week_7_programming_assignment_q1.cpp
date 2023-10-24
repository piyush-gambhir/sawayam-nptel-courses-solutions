#include <bits/stdc++.h>
#define gupt_forLoop(i, a, b) for(int i = a; i < b; i++)
#define gupt_longLong long long
#define gupt_modulus 1000000007
#define gupt_endLine std::cout << std::endl
using namespace std;

int gupt_primersAlgorithm(vector<vector<int>> gupt_edges[], bool gupt_isVisited[], int gupt_startVertex) {
    int gupt_totalCost = 0;
    set<vector<int>> gupt_priorityQueue;

    for (int i = 0; i < gupt_edges[gupt_startVertex].size(); i++) {
        gupt_priorityQueue.insert({gupt_edges[gupt_startVertex][i][1], gupt_startVertex, gupt_edges[gupt_startVertex][i][0]});
    }

    while (!gupt_priorityQueue.empty()) {
        auto gupt_edge = *(gupt_priorityQueue.begin());
        int gupt_vertexU = gupt_edge[1];
        int gupt_vertexV = gupt_edge[2];
        int gupt_weight = gupt_edge[0];

        gupt_priorityQueue.erase(gupt_priorityQueue.begin());

        if (!gupt_isVisited[gupt_vertexU] || !gupt_isVisited[gupt_vertexV]) {
            if (gupt_isVisited[gupt_vertexU] == false) {
                for (int i = 0; i < gupt_edges[gupt_vertexU].size(); i++) {
                    gupt_priorityQueue.insert({gupt_edges[gupt_vertexU][i][1], gupt_vertexU, gupt_edges[gupt_vertexU][i][0]});
                }
            }
            gupt_isVisited[gupt_vertexU] = true;

            if (gupt_isVisited[gupt_vertexV] == false) {
                for (int i = 0; i < gupt_edges[gupt_vertexV].size(); i++) {
                    gupt_priorityQueue.insert({gupt_edges[gupt_vertexV][i][1], gupt_vertexV, gupt_edges[gupt_vertexV][i][0]});
                }
            }
            gupt_isVisited[gupt_vertexV] = true;

            gupt_totalCost += gupt_weight;
        }
    }
    return gupt_totalCost;
}

int main() {
    int gupt_numberOfVertices, gupt_numberOfEdges;
    cin >> gupt_numberOfVertices >> gupt_numberOfEdges;

    vector<vector<int>> gupt_edges[gupt_numberOfVertices];
    gupt_forLoop(i, 0, gupt_numberOfEdges) {
        int gupt_vertexU, gupt_vertexV, gupt_weight;
        cin >> gupt_vertexU >> gupt_vertexV >> gupt_weight;

        gupt_edges[gupt_vertexU].push_back({gupt_vertexV, gupt_weight});
        gupt_edges[gupt_vertexV].push_back({gupt_vertexU, gupt_weight});
    }

    bool gupt_isVisited[gupt_numberOfVertices] = {false};

    int gupt_maxCost = INT_MIN;

    gupt_forLoop(i, 0, gupt_numberOfVertices) {
        if (gupt_isVisited[i] == false) {
            gupt_maxCost = max(gupt_maxCost, gupt_primersAlgorithm(gupt_edges, gupt_isVisited, i));
        }
    }

    cout << gupt_maxCost;

    return 0;
}