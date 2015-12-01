import os
from Crypto.Cipher import ARC4
import socket

host = ''
port = 1337
key = '12345'

def rtext():
    return os.urandom(4).encode('hex')

def encrypt(data):
    return ARC4.new(key).encrypt(data)

def decrypt(data):
    return ARC4.new(key).decrypt(data)
    

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(10)
while 1:
    client, address = s.accept()
    data = client.recv(1024)
    if data:
        print 'Server received', data
        cip = encrypt(data)
        if(client.send(cip)):
                    print 'sent',cip.encode('hex')
        ptext = rtext()
        if(client.send(ptext)):
            print 'sent', ptext.encode('hex')
        data = client.recv(1024)
        if data:
            print 'Server received', data.encode('hex')
        if(ARC4.new(key).decrypt(data) == ptext):
            print 'client authenticated.'
            exit(0)
    client.close() 
