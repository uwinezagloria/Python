temperature=40
if temperature > 30:
    print("it's warm")
    print("drink water")
elif temperature>20:
    print("it's nice") 
else :
    print("it's cold")
 # ternary operator   
age=10
message="eligible" if age >=10 else "not eligible"
print (message)
 # logical operator
high_income=True
good_credit=False
student=True
if high_income and good_credit:
    print("eligible")
else:
    print("not eligible")    
if high_income or good_credit:
    print("eligible")
else:
    print("not eligible")
if not student:
    print("you are not student") 
else:
    print("you are student")       
  