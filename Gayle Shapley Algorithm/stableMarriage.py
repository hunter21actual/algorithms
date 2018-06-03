# Solution to stable marriage problem using GS Algorithm
# Can be used to match n users to n servers and similar
# problems given individual preferences

def preference(mat, w, man, man1):
	man1_rank = 0
	for i in range(len(mat[w])):
		if(mat[w][i] == man1):
			man1_rank = i + 1
			break

	man_rank = 0
	for i in range(len(mat[w])):
		if(mat[w][i] == man):
			man_rank = i + 1
			break

	if(man_rank < man1_rank):
		return True
	return False

def stable_matching(mat, n):
	#M conatains match status of men
	M = [False for i in range(n)]

	#match conatins men - women pairing
	match = [[i + n, False] for i in range(n)]

	free = n
	while free > 0:

		# Select free men one by one
		man = 0
		for j in range(len(M)):
			if not M[j]:
				man = j
				break

		for i in range(n):
			if not M[man]:

				# check if the first preference of ith man is free
				# if yes pair them together
				woman = mat[man][i]
				if not match[woman - n][1]:
					match[woman - n][1] = man
					M[man] = True
					free -= 1

				# if woman is not free we check if she prefers ith man
				# over her current mate and pair accordingly
				else:
					man1 = match[woman - n][1]

					if preference(mat, woman, man, man1):
						match[woman - n][1] = False
						M[man] = True
						M[man1] = False

	for w in match:
		print(w)

# matrix containing preferences for males and females
# males are numbered 0,1,2,3 and females are numbered 4,5,6,7

mat = [[7,5,6,4],[5,4,6,7],[4,5,6,7],[4,5,6,7],[0,1,2,3],[0,1,2,3],[0,1,2,3],[0,1,2,3]]
stable_matching(mat,4)
