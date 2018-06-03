from socket import socket
import pickle

def big_mod(base, exponent, mod):
	res = 1
	while exponent:
		if(exponent % 2 == 1):
			res = (res*base) % mod
		exponent >>= 1
		base = (base*base) % mod
	return res % mod

# RSA encryption (ascii)^e mod phi(N)
# Please take a look at keyGenerator
def encrypt(message):
	msg = [big_mod(ord(ch), 76169, 153199) for ch in message]
	return msg

s = socket()
print("Socket created successfully.")

port = 12345

s.bind(('', port))
print("Socket binded to {}".format(port))

s.listen(5)
print("Listening for connections ...")

msg = encrypt('Rivest Shamir Adelman')
msg = pickle.dumps(msg)

while True:
	c, addr = s.accept()
	print("Connection from {}".format(addr))

	c.send(msg)

	c.close()
