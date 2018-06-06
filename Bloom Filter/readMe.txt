# Bloom Filter using 2 Hash functions

Basic description from Wikipedia

"A Bloom filter is a space-efficient probabilistic data structure, conceived by Burton Howard Bloom in 1970, that is used to test whether an element is a member of a set. False positive matches are possible, but false negatives are not – in other words, a query returns either "possibly in set" or "definitely not in set". Elements can be added to the set, but not removed (though this can be addressed with a "counting" filter); the more elements that are added to the set, the larger the probability of false positives."

A wonderful video explaining things:
https://www.youtube.com/watch?v=qBTdukbzc78

For my implimentation i have used:

1. 400 bit boolean array. N = 400.
2. 2 hash functions as explained below
    i. sum of the ascii values of the alphbets at even places mod N
    ii. sum of the ascii values of the alphbets at odd places mod N
3. 20 elements are to be inserted

For each word, the bits corresponding to the positions returned by the hash functions are set in the array.

Ideally the hash functions sould be independant to avoid collisons as much as possible thus reducing false positives.

Further reading:
https://en.wikipedia.org/wiki/Bloom_filter
