from fractions import gcd

# 1. Pick 2 prime nos. p and q

p = 239 
q = 641	

# Multiply them to get N which is the public key
N = p*q
phi = (p-1)*(q-1)

# Generate private key for server
keys = []
nums = [k for k in range(2, phi)]
for e in nums:
	if(gcd(e, N) == 1 and gcd(e, phi) == 1):
		keys.append(e)

e = keys[int(len(keys)/2)]

# Generate private key for client
dec = 0
for d in nums:
	if (d*e) % phi == 1 and d > 10000:
		dec = d
		break

# PLEASE DO NOT SHARE YOUR PRIVATE KEYS WITH ANYONE!

# Here are the sample results
print(e, d)
# e, d = 76169, 110009
print(N, phi)
# N, phi = 153199, 152320
