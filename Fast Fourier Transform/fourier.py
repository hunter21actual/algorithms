from math import * 
	
def reverse_bit(n, b):
    if(n == 0):
    	return n
    res = 0
    for i in range(b):
        res <<= 1
        if(n & 1):
            res += 1
        n >>= 1
    
    return res

def is_power_of_two(n):
	return not (n & (n-1))

def next_pow(num):
	i = 0
	while(num > 2**i):
		i += 1

	return i

def bit_reverse_copy(arr):
	if(is_power_of_two(len(arr))):
		n = len(arr)
		b = int(log2(n))
	else:
		b = next_pow(len(arr))
		n = 2**b
		for i in range(n - len(arr)):
			arr.append(0)

	A = [0]*n
	for k in range(n):
		A[reverse_bit(k, b)] = arr[k]
	return A

# pass fft(arr, 1) for inverse FFT and fft(arr) for just FFT
def fft(arr, inv = 0):
	A = bit_reverse_copy(arr)
	n = len(arr)
	x = [-1, 1]
	for s in range(1, int(log2(n)) + 1):
		m = 2**s
		wm = cos(2*pi*x[inv]/m) + 1j*sin(2*pi*x[inv]/m)
		for k in range(0, n, m):
			w = 1
			for j in range(0, int(m/2)):
				t = w*A[k+j+int(m/2)]
				u = A[k+j]
				A[k+j] = u + t
				A[k+j+int(m/2)] = u - t
				w = w*wm
	
	if(inv == 1):
		A = [z/n for z in A]
	A = [round(num.real, 2) + round(num.imag, 2) * 1j for num in A]
	return A

arr = [i+1 for i in range(0,5)]
ans = fft(arr)
for f in ans:
	print(f)

back = fft(ans, 1)
print('\n')
for samp in back:
	print(samp)


