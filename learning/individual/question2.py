"""Create a calculator that takes two 
numbers and performs addition, 
subtraction, multiplication, and 
division. Ensure all conditions are 
considered.
"""
# entering numbers by user
num1=float(input("Enter First Number: "))
num2=float(input("Enter Second Number: "))
sum=num1+num2
product=num1*num2
difference=num1-num2
#we can not divide by zero so we have to use condition
if num2 !=0:
    division=num1/num2
else :
    division="undefined"    
print(" Calculator Results: ")
print(f"Addition: {num1} + {num2} = {sum}")
print(f"Subtraction: {num1} - {num2} = {difference}")
print(f"Multiplication: {num1} × {num2} = {product}")
print(f"Division: {num1} ÷ {num2} = {division}")
