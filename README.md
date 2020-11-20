# auto-awd

Aiming at making AWD for pwn easy.

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
- Log system
- Flag submit system
- Argument support