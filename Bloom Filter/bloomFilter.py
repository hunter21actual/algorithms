# Bloom filter
# Special thanks: Atul Kumar, Geeks for Geeks

# Table below gives false positive probalilty for
# different array sizes

# Array size 	False positive prob. (in %)

# 	60					  23.957
#	110					  9.364
#	400					  0.908

# No. of insertions  = 20 (fixed)
# No. of hash functions = 2 (fixed)
N = 60

from random import shuffle

class BloomFilter:
	def __init__(self):
		# Bit array
		self.arr = [0]*N
	
	# First hash function
	# sum of the ascii values of the letters at even places mod N
	def h1(self, word):
		return sum(ord(word[i]) for i in range(0, len(word), 2)) % N
	
	# Second hash function
	# sum of the ascii values of the letters at odd places mod N
	def h2(self, word):
		return sum(ord(word[i]) for i in range(1, len(word), 2)) % N
	
	# Inserts word into bloom filter
	def insert(self, word):
		self.arr[self.h1(word)] = 1
		self.arr[self.h2(word)] = 1
	
	# Check if the word is present or not
	def lookup(self, word):
		if(self.arr[self.h1(word)] and self.arr[self.h2(word)]):
			return True
			#return "{} may be present.".format(word)
		#return "{} is not present".format(word)
		return False
	
	# Counts the no. of set bits in the array
	def ones(self):
		return sum(self.arr)


b = BloomFilter()

# words to be added
word_present = ['abound','abounds','abundance','abundant','accessable',
                'bloom','blossom','bolster','bonny','bonus','bonuses',
                'coherent','cohesive','colorful','comely','comfort',
                'gems','generosity','generous','generously','genial']
 
# word not added
word_absent = ['bluff','cheater','hate','war','humanity',
               'racism','hurt','nuke','gloomy','facebook',
               'geeksforgeeks','twitter']
 
for word in word_present:
	b.insert(word)
 
shuffle(word_present)
shuffle(word_absent)
 
test_words = word_present[:10] + word_absent

for word in test_words:
    if b.lookup(word):
        if word in word_absent:
            print("{} is a false positive!".format(word))
        else:
            print("{} is probably present!".format(word))
    else:
        print("{} is definitely not present!".format(word))
