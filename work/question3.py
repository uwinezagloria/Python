"""Exercises on Loops


➢ A sequence of numbers from 1 to 10 with a step of 3
➢ Print individual letters of a string "PYTHON"
➢ Given the list numbers = [2, 7,10, 16, 23, 54] print a list of squares of each number 
in the list
➢ Given the float_list = [2.5, 16.42, 10.77, 8.3, 34.21] print how many numbers 
are less than 10."""
#➢ The sequence of numbers from 1 to 10
print("sequence of numbers from 1 to 10")
for i in range(1,11):
    print(i)
#➢ A sequence of even numbers between 0 and 20 (inclusive)
print("sequence of even numbers between 0 and 20")
for j in range(0,21):
    if j%2==0:
        print(j)
#➢ A sequence of numbers from 1 to 10 with a step of 3
for n in range(1,11,3):
    print (n)
 #➢ Print individual letters of a string "PYTHON"
letters="PYTHON"
for letter in letters :
    print(letter)
 #➢ Given the list numbers = [2, 7,10, 16, 23, 54] print a list of squares of each number 
#in the list
numbers= [2, 7,10, 16, 23, 54]
square=[]
for num in numbers:
    square.append(num*num)
print(square)
#Given the float_list = [2.5, 16.42, 10.77, 8.3, 34.21] print how many numbers 
#are less than 10.
float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
count=0
for nbr in float_list :
    if(nbr<10):
        count=count+1
print("Numbers  that are less than 10 are :",count)
        