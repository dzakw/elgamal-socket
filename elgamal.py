import random
from math import pow

a=random.randint(2,10)

#To find gcd of two numbers
def gcd(a,b):
    if a<b:
        return gcd(b,a)
    elif a%b==0:
        return b
    else:
        return gcd(b,a%b)

#For key generation i.e. large random number
def gen_key(q):
    random.seed(32)
    key= random.randint(pow(10,20),q)
    while gcd(q,key)!=1:
        random.seed(32)
        key=random.randint(pow(10,20),q)
    return key

def power(a,b,c):
    x=1
    y=a
    while b>0:
        if b%2==0:
            x=(x*y)%c;
        y=(y*y)%c
        b=int(b/2)
    return x%c

#For asymetric encryption
random.seed(29)
q=random.randint(pow(10,20),pow(10,50))
random.seed(92)
g=random.randint(2,q)
k=gen_key(q)
h=power(g,k,q)

p=power(g,k,q)
key=gen_key(q)


def enc(msg,q,h,g):
    s=power(h,k,q)

    ct=[]
    for i in range(0,len(msg)):
        ct.append(msg[i])
    print("g^k used= ",p)
    print("g^ak used= ",s)
    for i in range(0,len(ct)):
        ct[i]=s*ord(ct[i])
    return ct,p

#For decryption
def dec(ct,p,key,q):
    pt=[]
    h=power(p,key,q)
    for i in range(0,len(ct)):
        pt.append(chr(int(ct[i]/h)))
    return pt