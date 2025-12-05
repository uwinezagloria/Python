#creeate new file if it does not exist "r" it read mode "w" it is weiting mode
file=open("example.txt","w")
file.write("hello everyone")
lines=["\n my name is uwineza","\n am 21 years old"]
file.writelines(lines)
