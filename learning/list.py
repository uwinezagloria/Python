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
list_numbers=[1,2,3,4,5,6,5,3]
#counting how many 5 are in the list
print(list_numbers.count(5)) # output:2
#sorting 
list_numbers.sort()
print(list_numbers) # sorted but when we print like print(list_numbers.sort()) it will return none which stands for absence of value so sort return none
#reversing
list_numbers.reverse()
print(list_numbers)
# checkin if certaun number is in the list
print(50 in list_numbers) # return False as 50 is not in the list
#deleting last element in list
list_numbers.pop()
#inserting item in list at a cetain index
list_numbers.insert(2,40)
print(list_numbers)
#finding index of certain value
print(list_numbers.index(5)) # if we have duplicates it will print index of first element to have that index
# removing dulplicates
for i in list_numbers:
    if  list_numbers.count(i)>1:
        list_numbers.remove(i)
print(list_numbers)  
#when you want a list of item and it will not be modified yo ucan use tuple
