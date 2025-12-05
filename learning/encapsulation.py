class Account:
    def __init__(self,balance=0):
        self.__balance=balance #private property
    def deposit(self,amount) : 
        if amount >0: 
           self.__balance+=amount
        return f"you have deposited:{amount}RWF on your account"
    def withdraw(self,amount):
        if amount<self.__balance and amount >0 :
           self.__balance-=amount    
        return f"you have with draw {amount}RWF" 
    def getbalance(self):
        return f"your current balance is {self.__balance}" 
person1=Account()
deposited=person1.deposit(20000) 
withdraw=person1.withdraw(1000)
print(deposited)    
print(withdraw)  
print(person1.getbalance())  
         