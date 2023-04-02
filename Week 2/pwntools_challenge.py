from pwn import *

BINARY = '<path_to_binary>'
IP, PORT = 'ctf99.cs.ui.ac.id', 10002
LOCAL = False
if not LOCAL:
	p = remote(IP, PORT)
print(p.recv().decode())
p.sendline(b'V')
print(p.recvline().decode())

i = 1
while True:
	prompt = p.recvline().decode()
	print(f"prompt: {prompt}")
	if "CSCE604258{" in prompt:
		print(f"Got flag: {prompt}!")
		break
	word = (prompt.split(" "))[-1][1:-2]
	print(f'{i}: {word}')
	p.sendline(word.encode())
	i += 1

p.close()							# Closes 'p'
# Happy Pwning :)
