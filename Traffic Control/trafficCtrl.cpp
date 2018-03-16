/*
        Traffic Control Algorithm                            

        1. Get edge weights                             
        2. Push weights into priority queue PQ          
        3. While PQ is not empty                        
            1. push top value into queue Q
        4. While Q is not empty                        
            1. pop values from queue and divide it by default duty cycle of Traffic light
        5. Go to 1
*/

#include <bits/stdc++.h>
using namespace std;

const int N = 3;
double loadArray[N];
double trafficTime[5][N+3];

struct edge
{
    int id;
    double load;
};

priority_queue <double> MAX_HEAP;
queue <double> Q;

// Function for updating weights in each iteration
void updateLoad(edge graph[], double loadArray[], int N)
{
    for(int i = 0; i < N ; ++i){
        graph[i].load = loadArray[i];
    }
}

// Function to find Edge weight
int findID(edge graph[], double k, int N){
    for(int i = 0; i < N; ++i)
        if(graph[i].load == k)
            return graph[i].id;
    return -1;
}

int main()
{
    struct edge e[N];

    e[0].id = 1;
    e[1].id = 2;
    e[2].id = 3;

    int cnt = 5;
    while(cnt){

        cout << "Iteration " << 5 - cnt + 1 << endl;
        // Get weights for roads
        for(int i = 0; i < N; ++i){
            cout << "Enter wt for edge" << i+1 << " = ";
            cin >> loadArray[i];
        }

        // Update weights for roads
        for(int i = 0; i < N; ++i){
            updateLoad(e, loadArray, N);
        }

        // Insert weights into maxheap
        for(int i = 0; i < N; ++i){
            MAX_HEAP.push(e[i].load);
        }

        // Send values to queue
        while(!MAX_HEAP.empty()){
            Q.push(MAX_HEAP.top());
            MAX_HEAP.pop();
        }

        // Calculate transit times for each signal
        double k;
        int i = 0;
        while(!Q.empty()){
            k =  Q.front();
            int j = findID(e, k, N);
            trafficTime[5 - cnt][i+3] = j;
            trafficTime[5 - cnt][i] = 10*k;
            //delay(10*k)
            cout << "Signal " << j <<  " time = " << trafficTime[5 - cnt][i] << endl;
            Q.pop();
            i++;
        }
        cout << endl;
        cout << endl;
        cnt--;
    }

    for(int i = 0; i < 5; ++i){
        for(int j = 0; j < 6; ++j)
            cout << trafficTime[i][j] << " ";
        cout << endl;
    }

    return 0;

}
