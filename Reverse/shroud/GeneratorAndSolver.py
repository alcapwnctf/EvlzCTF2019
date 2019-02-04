import string
import random

random.seed(1549065600)
charset=list(string.printable[:-6]+' ')

def newList(aList):
    newList=list()
    for i in aList:
        parity=1 if i[0].isupper() else 0
        val=0
        for j in i[1:]:
            if j.isupper():val^=1
        if parity==val:newList.append(i)
    
    return newList

def conv(message,id):
    binm=''
    for i in message[1:]:
        if i.isupper(): binm += '1'
        else: binm += '0'
    val=int(binm,2)
    
    return val^(ord(charset[id])), charset[id]

mlist=list()
wadustr="waduhekk"
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    for f in range(2):
                        for g in range(2):
                            for h in range(2):
                                val=""
                                if a==0:val+=wadustr[0].lower()
                                else: val+=wadustr[0].upper()
                                if b==0:val+=wadustr[1].lower()
                                else: val+=wadustr[1].upper()
                                if c==0:val+=wadustr[2].lower()
                                else: val+=wadustr[2].upper()
                                if d==0:val+=wadustr[3].lower()
                                else: val+=wadustr[3].upper()
                                if e==0:val+=wadustr[4].lower()
                                else: val+=wadustr[4].upper()
                                if f==0:val+=wadustr[5].lower()
                                else: val+=wadustr[5].upper()                                                       
                                if g==0:val+=wadustr[6].lower()
                                else: val+=wadustr[6].upper()
                                if h==0:val+=wadustr[7].lower()
                                else: val+=wadustr[7].upper()
                                mlist.append(val)

randomWaduList=random.sample(newList(mlist),95)

keydict=dict()
for i in range(len(randomWaduList)):
    key,character=conv(randomWaduList[i],i)
    # print "    waduhekkmap.insert(pair<string, int>(\"{}\", {}));".format(randomWaduList[i],key)
    keydict.update({character:key})

def getBinary(message):
    waduScript=""
    for i in message:
        key=keydict[i]
        sum=0
        binstr=bin(ord(i)^key)[2:].zfill(7)
        for i in binstr:
            if i=='1':sum+=1
        
        if sum%2:waduScript+='W'
        else:waduScript+='w'
        
        j=0
        if binstr[j]=='1':waduScript+='A'
        else:waduScript+='a'
        j+=1
        if binstr[j]=='1':waduScript+='D'
        else:waduScript+='d'
        j+=1
        if binstr[j]=='1':waduScript+='U'
        else:waduScript+='u'
        j+=1
        if binstr[j]=='1':waduScript+='H'
        else:waduScript+='h'
        j+=1
        if binstr[j]=='1':waduScript+='E'
        else:waduScript+='e'
        j+=1
        if binstr[j]=='1':waduScript+='K'
        else:waduScript+='k'
        j+=1
        if binstr[j]=='1':waduScript+='K'
        else:waduScript+='k'
        
        waduScript+=' '
    
    return waduScript

# print getBinary('echo Hello and welcome to WaduCast. Note that I only understand waduhekk')
# print getBinary('echo Tell me what to do??')
print getBinary("cat flag")