"""
try:
    o=open("C:/Users/sumitHP/Desktop/s.txt","r")
    j=0
    for i in o:
        if j<5:
           print(i)
           j+=1
    o.close()
except:
    if FileNotFoundError:
        print("file not found")
"""

o=open("C:/Users/sumitHP/Desktop/pyt.txt","w")
o.write("to wirite in phy.txt")
o.close()


    
