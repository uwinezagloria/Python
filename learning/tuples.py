#tuples are same as list but they can not be modified
tuple=(1,2,3)
print(tuple[0]  ) #output : 1
#tuple[0]=29   # output : TypeError: 'tuple' object does not support item assignment
#unpacking 
coordinate=(1,2,3)#tuple  that has 3 item
#unpacking can also work on list
x,y,z=coordinate # same as x=coordinate[0] y=coordinate[1] z=coordinate[2]
print(x) 
print(y)
print(z)  
print(x*y*z) # output 6