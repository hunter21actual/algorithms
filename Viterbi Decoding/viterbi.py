# Viterbi decoding 
# Special thanks - Prof. Noor Mohammed, Ashish Korakana

#no. Of states
N = 4
# no. Of characters to be decoded
n = 8       
INF = 1000000

toDecode = ["100", "110", "111", "101", "001", "101", "001", "010"]
decode = [0]*(n+1)
edgeChk = [[0 for i in range(2)] for j in range(N+1)]
viterbi = [[INF for i in range(n+1)] for j in range(N+1)]
edgeChkMatrix = [[0 for i in range(N+1)] for j in range(N+1)]
key = {1 : "a", 2 : "b", 3 : "c", 4 : "d"}

def hammDist(str1, str2):
    cnt = 0;
    for i in range(0, len(str1)):
        if(str1[i] != str2[i]):
            cnt = cnt + 1
    return cnt


# edgeChkacency matrix of bipartite graph
# this was created to check if states are connected
edgeChkMatrix[1][1] = 1;
edgeChkMatrix[1][2] = 1;

edgeChkMatrix[2][3] = 1;
edgeChkMatrix[2][4] = 1;

edgeChkMatrix[3][1] = 1;
edgeChkMatrix[3][2] = 1;

edgeChkMatrix[4][3] = 1;
edgeChkMatrix[4][4] = 1;


# State Assignment
#state - 'a'
edgeChk[1][0] = "000";
edgeChk[1][1] = "111";

#state - 'b'
edgeChk[2][0] = "001";
edgeChk[2][1] = "110";

#state - 'c'
edgeChk[3][0] = "010";
edgeChk[3][1] = "101";

#state - 'd'
edgeChk[4][0] = "011";
edgeChk[4][1] = "100";


# Create path matrix to store details of each decoding iteration
viterbi[1][0] = 0;

viterbi[1][1] = viterbi[1][0] + hammDist(toDecode[0], edgeChk[1][0]);
viterbi[2][1] = hammDist(toDecode[0], edgeChk[1][1]);

viterbi[1][2] = viterbi[1][1] + hammDist(toDecode[1], edgeChk[1][0]);
viterbi[2][2] = viterbi[1][1] + hammDist(toDecode[1], edgeChk[1][1]);
viterbi[3][2] = viterbi[2][1] + hammDist(toDecode[1], edgeChk[2][0]);
viterbi[4][2] = viterbi[2][1] + hammDist(toDecode[1], edgeChk[2][1]);


for i in range(3, n + 1):
    viterbi[1][i] = min(viterbi[1][i-1] + hammDist(toDecode[i-1], edgeChk[1][0]), viterbi[3][i-1] + hammDist(toDecode[i-1], edgeChk[3][0]));
    viterbi[2][i] = min(viterbi[1][i-1] + hammDist(toDecode[i-1], edgeChk[1][1]), viterbi[3][i-1] + hammDist(toDecode[i-1], edgeChk[3][1]));
    viterbi[3][i] = min(viterbi[2][i-1] + hammDist(toDecode[i-1], edgeChk[2][0]), viterbi[4][i-1] + hammDist(toDecode[i-1], edgeChk[4][0]));
    viterbi[4][i] = min(viterbi[2][i-1] + hammDist(toDecode[i-1], edgeChk[2][1]), viterbi[4][i-1] + hammDist(toDecode[i-1], edgeChk[4][1]));


# backtracking to find best possible state
traceBack = [];
MIN = 1000000;
index = 0;
for j in range(1, N+1):
    if(viterbi[j][n] < MIN):
        MIN  = viterbi[j][n]
        index = j
   
traceBack.append(index)

cnt = 0;
for i in range(n-1, 0, -1):
    MIN = 1000000;
    index = 0;
    for j in range(1, N+1):
        # Condition to check connectivity between states
        if(viterbi[j][i]  <= MIN and edgeChkMatrix[j][traceBack[cnt]] == 1 and viterbi[j][i] + hammDist(toDecode[i],edgeChk[j][(traceBack[cnt] - 1)%2]) == viterbi[traceBack[cnt]][i+1]):
            MIN  = viterbi[j][i]
            index = j
    traceBack.append(index)
    cnt = cnt + 1

traceBack.append(1)

# state diagram
traceBack.reverse()

stateSequence = []
print("State sequence = ")
for i in range(len(traceBack)):
    stateSequence.append(key[traceBack[i]])

print(stateSequence)

#decoded output
print("\n")
print("Decoded output = ")
for i in range(1, n+1):
    decode[i] = edgeChk[traceBack[i-1]][(traceBack[i] - 1) % 2]

print(decode[1:])
