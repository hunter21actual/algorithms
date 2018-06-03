Iterative Fast Fourier Transform

Complexity of std DFT = O(n^2)
Complexity of Cooley-Tukey FFT = O(n*lg(n))

Refer to:

https://en.wikipedia.org/wiki/Cooley%E2%80%93Tukey_FFT_algorithm

A radix-2 decimation-in-time (DIT) FFT is the simplest and most common form of the Cooley–Tukey algorithm.
This is an example of an iterative Radix-2 FFT using bit-reversal permutation.

A few points to consider:

1. Ideally array size should be a power of 2
2. If it isn't a power of 2 some corrections have been made to compensate
  by padding zeros to make the array size a power of 2.
  
Other Complex algorithms exist for dealing with cases where array size is not a power of 2.

Further Reading:

https://en.wikipedia.org/wiki/Fast_Fourier_transform

https://math.stackexchange.com/questions/1704788/complexity-of-fft-algorithms-cooley-tukey-bluestein-prime-factor
