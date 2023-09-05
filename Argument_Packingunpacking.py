"""
#Arguments Packing

def sum(*nos):
    k=0
    for i in nos:
        k+=i
    return k

# after run this program you call from terminal as ""sum(2,3,4)""

print("Call the sum funtion with any no of arguments:")
"""

#Argument Unpacking

def area(l,b):
    return 2**b

l=int(input("provide length: "))

b=int(input("provide breath: "))
nos=(l,b)
print(area(*nos))

