# Adaptive Huffamn Encoding
# Information theory and coding
# Prof. Noor Mohammed

codes = []

#Encoding subroutine
def encode(key):
	k = ord(key) - 96
	val, cond, sub = k, [4, 5], [11, 1]
	k -= sub[val <= 20]
	bi = ''
	while(k):
		bi = str(k%2) + bi
		k //= 2
	while(len(bi) != cond[val <= 20]):
		bi = '0' + bi
	return bi

class Node:
	track = []
	def __init__(self, root = 1):
		self.root = root
		self.left = None
		self.right = {}

	def insert(self, key):
    # initial node
		if(not self.left and not bool(self.right)):
			self.track.append(key)
			self.right = {key: 1}
			self.left = None
			codes.append(encode(key))
			return

		temp = self
		code = ''
    # if node is already present in the tree
		if key in Node.track:
			while(True):
				if(type(self.right) == dict and key not in list(self.right.keys())):
					self.root += 1
					self = self.left
					code += '0'
				elif(type(self.left) == dict and key not in list(self.left.keys())):
					self.root += 1
					self = self.right
					code += '1'
				else:
					if(type(self.right) == dict):
						self.right[key] += 1
						self.root += 1
						code += '1'
						codes.append(code)
					else:
						self.left[key] += 1
						self.root += 1
						code += '0'
						codes.append(code)
					break
		
    # if node is not present in tree
		else:
			Node.track.append(key)
			while(self.left):
				if(type(self.right) == dict):
					self.root += 1
					self = self.left
					code += '0'
				elif(type(self.left) == dict):
					self.root += 1
					self = self.right
					code += '1'
			self.root += 1
			self.left = Node()
			self.left.left = None
			self.left.right = {key : 1}
			code += '0'
			code += encode(key)
			codes.append(code)
    
    # balancing the tree
		self = temp
		self.correct_tree()
		
	def print_tree(self):
		while(self):
			if(type(self.right) == dict):
				print(self.root, self.right, 'right')
				self = self.left
			else:
				print(self.root, self.left, 'left')
				self = self.right

  # correct tree subroutine. Tree should be right heavy
  # and right root value should be greater than left root value
	def correct_tree(self):
		if not self.left:
			return None
    
    # case 1 : if left root is greater than right dict value
		if(self.right and type(self.right) == dict):
			if(self.left.root > list(self.right.values())[0]):
				temp = self.right
				self.right = self.left
				self.left = temp
				self = self.right
				self.correct_tree()
			elif(self.left):
				self = self.left
				self.correct_tree()
    
    # case 2 : if right root is less than left dict value
		elif(self.left and type(self.left) == dict):
			if(self.right.root < list(self.left.values())[0]):
				temp = self.left
				self.left = self.right
				self.right = temp
				self = self.left
				self.correct_tree()
			elif(self.right):
				self = self.right
				self.correct_tree()

		return None

string = 'massachussets'

tree = Node()

# Uncomment to see the whole encoding procedure
for i in range(len(string)):
# 	print(string[i])
 	tree.insert(string[i])
# 	tree.print_tree()
# 	print()

st = ''
for c in codes:
	st += c

print(st)
