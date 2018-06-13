# LZW dictionary based encoding

string = input('')
track = list(set(string))                               # keeps track of keys
track.sort()      
hashset = {track[i]: i + 1 for i in range(len(track))}  # dictionary of indices
count = len(track) 
codes = []                                               # stores encoded information

current_index, next_index = 0, 1
while(next_index <= len(string)):
	i = 1
	while(string[current_index : current_index + i] in track and current_index + i <= len(string)):
		i += 1

	if(current_index + i - 1 == len(string)):
		track.append(string[current_index : current_index + i] + '#')
	else:
		track.append(string[current_index : current_index + i])
	cur = string[current_index : current_index + i - 1]
	nxt = string[current_index : current_index + i][-1]
	codes.append(hashset[cur])
	count += 1
	if(current_index + i - 1 == len(string)):
		hashset[cur + '#'] = count
	else:
		hashset[cur + nxt] = count
	current_index += (i - 1)
	next_index = current_index + 1

print(track)
print(hashset)
print(codes)

# Codes can be converted into binary easily but have been omitted for sake of clarity.
