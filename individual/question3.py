"""Student Grade Evaluator: Input a 
student’s marks in five subjects, 
calculate the average, and assign a 
grade based on the average using if elif-else. Store marks in a list and use a 
function to compute the average.
"""
def find_average(marks):
    total=sum(marks) #calculating sum of all marks
    average=total/len(marks) #calculating avarage
    return average # function will return the calculated average
print("Enter your marks in five subject: ")
marks=[] # empty list 
#loop to enter marks of 5 subject
for i in range(1,6 ): 
    mark=float(input("Enter marks:"))
    marks.append(mark) # adding  each mark in the marks list
 #calling find average function   
average=find_average(marks) 
# checking grade basing on average
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"
print(f" Your Marks: {marks}")
print(f" Your Average: {average:.2f}")
print(f"Your Grade: {grade}")    