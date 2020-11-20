# auto-awd

Aiming at making AWD for pwn easy.

Just write your local debug pwn script and `auto-awd` will help you to attack remote targets without altering your script.

# Requirement

- Put your `from pwn import *` or `from PwnContext import *` into your exploit without indent(not tab no space). If you are using your own imported pwnscript, add `from pwn import *` behind it.
- Make sure your script runs successfully.

# Technique

Auto hook `process` and `remote` of pwntools, and adapt them to your target machine(s).

# Usage

```sh
./auto-awd exploit.py 192.168.1.5 8888
```

## Test
```sh
nc -lvp -e /bin/sh 1234 # or use socat if your nc does not support -e
./auto-awd test.py localhost 1234
```

# TODO

- Multi thread support ( nessessary ? )
- Flag submit system