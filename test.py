from pwn import *

p = process('/bin/sh')
p.sendline('ls')
p.sendline(p32(0xdeadbeef))
print p.recv()
x = 1/0