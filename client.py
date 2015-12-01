#!/usr/bin/env python
import socket
import os
from Crypto.Cipher import ARC4

host = 'localhost'
port = 1337
key = '12345'

def rtext():
    return os.urandom(4).encode('hex')

def encrypt(data):
    return ARC4.new(key).encrypt(data)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
plaintext = rtext()
s.send(plaintext) #sending plaintext
print 'sent: ', plaintext.encode('hex')
data = s.recv(1024) #receiving cipher text from server
print 'Received:', data.encode('hex')
ptext = ARC4.new(key).decrypt(data) #printing by decrypting
print 'decrypted data:' + ptext
if(ptext == plaintext):
    print 'server authenticated.'
data = s.recv(1024)
if data:
    print 'received', data.encode('hex')
    cip = encrypt(data)
    if(s.send(cip)):
        print 'sent encrypted data: ', cip.encode('hex')
s.close()
