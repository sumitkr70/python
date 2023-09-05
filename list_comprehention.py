#list comprihention
'''
#program-1 of list comprihention

def squire(lst):
    new_list=[i**2 for i in lst]
    return(new_list)

nos=[2,3,4,5,6]
sq_list=squire(nos)

print(nos)
print(sq_list)
'''

#program-2

list1=["apple","banana","papaya","mango","kiwi","cherry"]
new_lst=[i for i in list1 if "a" in i]
print(new_lst)

