import string
import random

random.seed(1549065600)
numlist=[int(x) for x in range(1,101)]
vertices=random.sample(numlist,56)
flag="evlz{I_Jus7_Put_4_c0mpet1t1v3_Qu3st10n_in_cTf}ctf"

# for i in range(0,len(vertices),8):
# 	print "How do I go from {} to {}".format(vertices[i], vertices[i+7]) 

flagpartvertexlist=[]

for i in range(0,len(vertices),8):
	atuple=()
	for j in range(8):
		atuple+=(vertices[j+i],)
	flagpartvertexlist.append(atuple)

# print flagpartvertexlist

finaltuplelist=[]
charset=list("abcdefghijklmnopqrstuvwxyz}ABCDEFGHIJKLMNOPQRSTUVWXYZ{0123456789_")

for i in range(len(flagpartvertexlist)):
	for j in range(len(flagpartvertexlist[i])-1):
		
		char=charset[random.randint(0,len(charset)-1)]
		finaltuplelist.append((flagpartvertexlist[i][j],flagpartvertexlist[(i+1)%len(flagpartvertexlist)][j],char))
		finaltuplelist.append((flagpartvertexlist[(i+1)%len(flagpartvertexlist)][j],flagpartvertexlist[i][j],char)) #whoose
		
		char=charset[random.randint(0,len(charset)-1)]
		finaltuplelist.append((flagpartvertexlist[i][j],flagpartvertexlist[(i+1)%len(flagpartvertexlist)][j+1],char))
		finaltuplelist.append((flagpartvertexlist[(i+1)%len(flagpartvertexlist)][j+1],flagpartvertexlist[i][j],char))

pos=0
for i in flagpartvertexlist:
	for j in range(len(i)-1):
		finaltuplelist.append((i[j],i[j+1],flag[pos]))

		finaltuplelist.append((i[j+1],i[j],flag[pos]))
		pos+=1

finaltuplelist=random.sample(finaltuplelist,len(finaltuplelist))

#print finaltuplelist

for i in finaltuplelist:
    print "graph[{}][{}]='{}';".format(i[0],i[1],i[2])