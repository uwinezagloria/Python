firstname="Gloria"
print(firstname[0:4:2])
my_string = "This is My String !"
print(my_string[0])
#print(my_string[len(my_string)]) # error it is out of the range 
#How would I print the last ! Mark in my_string variable
print(my_string[len(my_string) - 1])
print(my_string[-1])
print(my_string[1:7])
print(my_string[0:7:2])
print(my_string[13:2:-1])
print(my_string[17:0:-2])
print(my_string[:])
print(my_string[:: -1]) # reversing
#Write a simple program that prints the total number of characters of a string entered by the user.
user=input("Enter string : ")
print(len(user))