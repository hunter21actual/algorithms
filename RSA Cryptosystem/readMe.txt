For details about the algorithm please visit the following link
in which Mr. Eddie Woo explains the RSA algorithm in 2 parts

part 1:

https://www.youtube.com/watch?v=4zahvcJ9glg

part 2:

https://www.youtube.com/watch?v=oOcTVTpUsPQ&t=571s

Also please subscribe to his channel for fun math videos

Process:

1. Generate private keys e and d for server and client respectively.
2. Send the message after encryption through a socket when a client makes a request.
3. Message is decrypted at Client window

Please note:- message is sent through a socket in the form of bytes.
Therefore any info other than a string has to be manually converted.
I have done this using pickling. For more info visit:

https://stackoverflow.com/questions/38412887/how-to-send-a-list-through-tcp-sockets-python
