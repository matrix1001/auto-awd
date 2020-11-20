from pwn import *

p = process('/bin/sh')
p.sendline('ls')
print p.recv()
p.close()