n=input("enter one no. of any digits, Which you wants to reverse: ")
l=len(n)
c=0
rn=0
p=0


for i in n:
    c=int(int(i)*(10**p))
    p=p+1
    rn=rn+c

s=str(rn)
t=len(s)
k=l-t


#print("you can assume {0} zero as prifix of your reversed number {1}".format(l-t,rn))
rn1=str(rn)
a=str(0)*k
pp=a+rn1
print("final no after reverse is: ",pp)


