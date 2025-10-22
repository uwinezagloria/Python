secret_number=4
count=0
i=1
while i<=3:
     gues=int(input("Guess:"))
     if gues==secret_number:
        print("You won!!")
        break 
     i+=1
else : # while loop can have an else 
    print(" sorry you Failed")         
        
         
        
     
             