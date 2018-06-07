# Run length encoding
# Compresses a string by keeping track of continous occurances
# replaces a substring of contiunuous occurances by only the character
# followed by the number of occurances
# for eg: eeeerrtttttv becomes e4r2t5v1

some_string = 'aaaawwwwaacccccvvbbb'

def run_length_encoding(string):
    res = string[0]
    cnt = 1
    
    for i in range(1,len(string)):
        if(string[i] == string[i-1]):
            cnt += 1
        else:
            res += str(cnt)
            res += string[i]
            cnt = 1
    res += str(cnt)
    return res

print(run_length_encoding(some_string))
