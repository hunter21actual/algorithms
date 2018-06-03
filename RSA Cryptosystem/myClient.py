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


def decrypt(message):
	msg = [chr(big_mod(ch, 110009, 153199)) for ch in message]
	return ''.join(msg)

s = socket()
port = 12345

s.connect(('127.0.0.1', port))
msg = s.recv(1024)

# Since data is sent as bytes by pickling we need to unpickle
msg = pickle.loads(msg)
msg = decrypt(msg)
print(msg)
s.close()
