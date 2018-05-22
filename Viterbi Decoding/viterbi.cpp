#include <bits/stdc++.h>
using namespace std;

#define N 4
#define n 8
#define INF 1000000

string toDecode[n] = {"100", "110", "111", "101", "001", "101", "001", "010"};
string result[n];
string adj[N + 1][2];
int pathMatrix[N + 1][n + 1];
int adjMatrix[N+1][N+1];
map <int, string> decipher;

void initializeArray(int pathMatrix[][n+1])
{
    for(int i = 0; i <= N; ++i)
        for(int j = 0; j <= n; ++j)
            pathMatrix[i][j] = INF;

}

int getHammingDistance(string str1, string str2)
{
    int cnt = 0;
    int len = str1.length();
    for(int i = 0; i < len; ++i)
        if(str1[i] != str2[i])
            cnt++;
    return cnt;
}

int main()
{
    // construct state diagram / graph

    // mapping of numbers to symbols
    decipher[1] = "a";
    decipher[2] = "b";
    decipher[3] = "c";
    decipher[4] = "d";

    // adjacency matrix of bipartite graph
    // this was created to check if states are connected
    adjMatrix[1][1] = 1;
    adjMatrix[1][2] = 1;

    adjMatrix[2][3] = 1;
    adjMatrix[2][4] = 1;

    adjMatrix[3][1] = 1;
    adjMatrix[3][2] = 1;

    adjMatrix[4][3] = 1;
    adjMatrix[4][4] = 1;

    // State Assignment
    //state - 'a'
    adj[1][0] = "000";
    adj[1][1] = "111";

    //state - 'b'1
    adj[2][0] = "001";
    adj[2][1] = "110";

    //state - 'c'
    adj[3][0] = "010";
    adj[3][1] = "101";

    //state - 'd'
    adj[4][0] = "011";
    adj[4][1] = "100";

    // Initialize matrix
    initializeArray(pathMatrix);

    // Create path matrix to store each decoding iteration
    pathMatrix[1][0] = 0;

    pathMatrix[1][1] = pathMatrix[1][0] + getHammingDistance(toDecode[0], adj[1][0]);
    pathMatrix[2][1] = getHammingDistance(toDecode[0], adj[1][1]);

    pathMatrix[1][2] = pathMatrix[1][1] + getHammingDistance(toDecode[1], adj[1][0]);
    pathMatrix[2][2] = pathMatrix[1][1] + getHammingDistance(toDecode[1], adj[1][1]);
    pathMatrix[3][2] = pathMatrix[2][1] + getHammingDistance(toDecode[1], adj[2][0]);
    pathMatrix[4][2] = pathMatrix[2][1] + getHammingDistance(toDecode[1], adj[2][1]);

    for(int i = 3; i <= n; ++i){
        pathMatrix[1][i] = min(pathMatrix[1][i-1] + getHammingDistance(toDecode[i-1], adj[1][0]),
                               pathMatrix[3][i-1] + getHammingDistance(toDecode[i-1], adj[3][0]));
        pathMatrix[2][i] = min(pathMatrix[1][i-1] + getHammingDistance(toDecode[i-1], adj[1][1]),
                               pathMatrix[3][i-1] + getHammingDistance(toDecode[i-1], adj[3][1]));
        pathMatrix[3][i] = min(pathMatrix[2][i-1] + getHammingDistance(toDecode[i-1], adj[2][0]),
                               pathMatrix[4][i-1] + getHammingDistance(toDecode[i-1], adj[4][0]));
        pathMatrix[4][i] = min(pathMatrix[2][i-1] + getHammingDistance(toDecode[i-1], adj[2][1]),
                               pathMatrix[4][i-1] + getHammingDistance(toDecode[i-1], adj[4][1]));
    }

    // backtracking to find best possible state
    vector <int> minPath;
    int MIN = 1000000;
    int index = 0;
    for(int j = 1; j <= N; ++j){
        if(pathMatrix[j][n] < MIN){
            MIN  = pathMatrix[j][n];
            index = j;
        }
    }
    minPath.push_back(index);

    int cnt = 0;
    for(int i = n - 1; i >= 1; i--){
        int MIN = 1000000;
        int index = 0;
        for(int j = 1; j <= N; ++j){
            // Condition to check connectivity between states
            if(pathMatrix[j][i]  <= MIN && adjMatrix[j][minPath[cnt]] == 1 
            && pathMatrix[j][i] + getHammingDistance(toDecode[i], adj[j][(minPath[cnt]-1)%2]) == pathMatrix[minPath[cnt]][i+1]){
                MIN  = pathMatrix[j][i];
                index = j;
            }
        }
        minPath.push_back(index);
        cnt++;
    }
    minPath.push_back(1);
    // state diagram
    reverse(minPath.begin(), minPath.end());

    cout << "State sequence = ";
    for(unsigned int i = 0; i < minPath.size() - 1; ++i)
        cout << decipher[minPath[i]] << " -> ";

    cout << decipher[minPath[n]] << endl;

    //decoded output
    cout << endl;
    cout << "Decoded output = ";
    for(int i = 1; i <= n; ++i)
        result[i] = adj[minPath[i-1]][(minPath[i] - 1) % 2];

    for(unsigned int i = 1; i < minPath.size(); ++i)
        cout << result[i] << " ";
    cout << endl;

    return 0;
}
