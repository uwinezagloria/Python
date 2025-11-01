myList=[1,"apple",3]
print(myList)
#adding element at the end of list we use append
myList.append("banana")
print(myList)
#removing element in a list
myList.remove("banana")
print(myList)
#Write a Python program to sum all the items in a list.
numbers=[1,2,3,4,5]
sum=0
for i in numbers:
    sum+=i
print(sum)    
#Get Largest Number in List
print(max(numbers))
#Get Smallest Number in List
print(min(numbers))
# Count Strings with Same Start and End
list=['abc', 'xyz', 'aba', '1221']
count=0
for i in list:
    if i[0]==i[-1] :
        count +=1
print(count)  
#. Convert List to String we use join method
string=''.join(list)
print(string)  
    
