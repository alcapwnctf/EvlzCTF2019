import random
import binascii
import base64
import textwrap

def strtobin(data):
    b_data = ""
    
    for i in range(len(data)):
        b_data += bin(ord(data[i]))[2:].zfill(7)

    m = len(b_data)%240
    X_str = b_data[:(-m)]
    X_list = textwrap.wrap(X_str,240)
    return(X_list)

def message_schedule(X_list_i):
    
    def shift(s, n):
        return(s[n:] + s[:n])
    
    W = []
    X_list_divided = textwrap.wrap(X_list_i,30)
    
    #insert_code_here
    
    return(W)


def Round_function(ABCD,S_C,Keyword,):
    A = ABCD[0]
    B = ABCD[1]
    C = ABCD[2]
    D = ABCD[3]
    
    def shift(s, n):
        return(s[n:] + s[:n])
    
    def ADD(p,q,r):
        p = int(str(p),2)
        q = int(str(q),2)
        r = int(str(r),2)
        return(str(bin(p+q+r))[3:])
        
    
    def AND(p,q):
        p = int(str(p),2)
        q = int(str(q),2)
        return(str(bin(p&q))[2:])
    
    def OR(p,q):
        p = int(str(p),2)
        q = int(str(q),2)
        return(str(bin(p|q))[2:])
    
    def XOR(p,q):
        p = int(str(p),2)
        q = int(str(q),2)
        return(str(bin(p^q))[2:])
    
    
    def func(a,b,c,d,S_C,Keyword,S_F):
        
        #insert_code_here
        
        return(d4)
    
    A #= insert_code_here
    B #= insert_code_here
    C #= insert_code_here
    D #= insert_code_here
    
    ABCD = [A,B,C,D]
    
    return(ABCD)


def MHA(X):
    K1 = "011111000010000011011101011010"  #"7C20DD68" -2 bits 
    K2 = "110110001111100110101000101011"  #"D8F9A8AF" -2 bits
    K3 = "100110011111011000011111010111"  #"99F61F5C" -2 bits
    K4 = "101001111010101100000010110010"  #"A7AB02C9" -2 bits
    Base64 = "ABCDEFGHIJKLMNOPQRSTUVWXZYabcdefghijklmnopqrstuvwxyz0123456789+/"
    Stage_constant = []
    
    IV = K3 + K2 + K4 + K1 
    
    X_list = strtobin(X)
    
    for i in range(len(X_list)):
        
        W_list = message_schedule(X_list[i])
        
        if i == 0:
            ABCD = textwrap.wrap(IV,30)
        
        else:
            ABCD = textwrap.wrap(Xi_l,30)
            
        #insert_code_here
            
        Xi_1 = "".join(ABCD)
    
    
    H1 = textwrap.wrap(Xi_1,6)
    HASH = ""
    
    for i in range(len(H1)):
        HASH += Base64[int(H1[i],2)]
        
    HASH = binascii.hexlify(HASH.encode())
    
    print("Hash:",HASH.decode())