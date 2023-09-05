n=int(input("enter any no, Print all the prime no between 1 to n: "))

for j in range(2,n+1):
    for i in range(2,j):
        if j%i==0:
            break
    else:
        print(j)
    
'''
n=int(input("enter any no and check it is a prime no or not? : "))
i=2
while i<n:
    if n%i==0:
        print("{0} is not a prime no.".format(n))
        break
    i+=1
else:
    print("{0} is a prime no.".format(n))

'''
