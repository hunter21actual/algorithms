# LZ - 78 dictionary based encoding

string = input('')
stk = list(set(string))
stk.sort()
hashset = {stk[i]: i + 1 for i in range(len(stk))}  # Dictionary of indices
count = len(stk)
codes = []     # stores encoded information
track = []     # keeps track of keys encountered so far

ptr = 0
while(ptr <= len(string) - 1):
	if string[ptr] not in track:
		track.append(string[ptr])
		codes.append({0 : string[ptr]})
		ptr += 1
		
	else:
		i = 1
		while(string[ptr:ptr+i] in track and  ptr + i <= len(string)):
			i += 1
		track.append(string[ptr:ptr + i])
		codes.append({hashset[string[ptr: ptr + i-1]] : string[ptr:ptr + i][-1]})
		count += 1
		hashset[string[ptr:ptr + i]] = count
		ptr = ptr + i

for code in codes:
	print(code)

# Further conveersion to binary can be done easily but has been omitted for sake of clarity
