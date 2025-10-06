first = "Hello"
second = "World"
print(first + " " + second)  # joining strings
laugh = "ha"
print(laugh * 3)   # hahaha #repetion
string="hello,world"
print(string[0:4]) #slicing
#getting length of string
print(len(string))
first_name="Gloria"
last_name="Uwineza"
full=f" {first_name} {last_name} " #formatted string with expression
print(full)
#string methods
print(full.title) # value of variable full
print(full.upper()) #uppercase
print(full.lower()) #lowercase
print(full.strip()) #trim beggining and end space
print(full.lstrip()) # remoce left space
print(full.rstrip()) # remove right space
print(full.find("pro")) # seaching index of pro if it exit it return index of it otherwise it returns -1
print(full.replace("a","b")) # replaceing a in full with b
print("glo" in full) #false if we don't have glo 
print("glo" not in full)# true when we dn't have glo in full