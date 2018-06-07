# Huffaman Encoding
# ECE - Information Theory and Coding (Winter - 2018)

# Symbols and their corresponding probability
#Xp = {'x1': 0.37, 'x2': 0.33, 'x3': 0.16, 'x4': 0.07, 'x5': 0.04, 'x6': 0.02, 'x7': 0.01}
Xp = {'x1': 0.4, 'x2': 0.2, 'x3': 0.1, 'x4': 0.1, 'x5': 0.1, 'x6': 0.05, 'x7': 0.05}
#Xp = {'x1': 0.4, 'x2': 0.2, 'x3': 0.2, 'x4': 0.1, 'x5': 0.07, 'x6': 0.03}
#Xp = {'x1': 0.3, 'x2': 0.2, 'x3': 0.2, 'x4': 0.15, 'x5': 0.15}

# WARNING :- Ensure that the probabilities add up to 1.

sym = sorted(Xp, key = lambda x : Xp[x], reverse = True)
Xp = {x : Xp[x] for x in sym}     # Stores symbols in decresing order of probability

# array stores successive iterations.
# Last 2 elements are added and assigned position such that probability of symbols below
# are less than or equal to the probability of added elements

array = [[0]*i for i in range(len(Xp), 0, -1)]

# Captures the sequence. Using he last 2 elements of each list in mat symbols are
# assigned 1 and 0.
mat = [[0]*i for i in range(len(Xp), 1, -1)]

symbols = ['']*len(Xp) # Contains the encoded symbols

mat[0][-2] = [len(Xp) - 1]
mat[0][-1] = [len(Xp)]

array[0] = [Xp[x] for x in Xp]
for i in range(1, len(Xp) - 1):
    place = array[i-1][-1] + array[i-1][-2]

    j = len(array[i-1]) - 2
    while(place >= array[i-1][j] and j >= 0):
        j -= 1
    
    # Sum of the lowest two is placed at the right place
    array[i][j+1] = place
    mat[i][j+1] = mat[i-1][-1] + mat[i-1][-2]
    
    if(j+1 == len(array[i]) - 1):
        mat[i][j] = [j+1]
      
    k = 0
    # Elements with probability greater than place are copied as it is
    while(k <= j):
        array[i][k] = array[i-1][k]
        k += 1
    
    k += 1
    # Elements with probability less than the sum are shifted diagonally down
    while(k < len(array[i])):
        array[i][k] = array[i-1][k-1]
        mat[i][k] = [k]
        
        if(k == len(array[i]) - 2):
            if(type(mat[i-1][k-1]) == list):
            	mat[i][k] = mat[i-1][k-1]
            else:
            	mat[i][k] = [k]
            
        if(k == len(array[i]) - 1):
            if(type(mat[i-1][k-1]) == list):
            	mat[i][k] = mat[i-1][k-1]
            else:
            	mat[i][k] = [k]
            
        k += 1

for arr in mat:
    m1 = arr[-1]
    m2 = arr[-2]
    for m in m1:
        symbols[m-1] += '0'
    for m in m2:
        symbols[m-1] += '1'

symbols = [sy[::-1] for sy in symbols]

for i in range(len(symbols)):
    print(sym[i],symbols[i])
