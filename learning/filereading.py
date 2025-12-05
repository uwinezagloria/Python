#reading wha is in file
reading=open("example.txt","r")
content=reading.read()
print(content)
lines=reading.readlines()
print(lines)