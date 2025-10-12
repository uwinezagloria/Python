""" . In this Exercise, you must discount a price according to its value.
➢ If the price is 300 or above, there will be a 30% discount.
➢ If the price is between 200 and 300 (200 inclusive), there will be a 20% discount.
➢ If the price is between 100 and 200 (100 inclusive), there will be a 10% discount.
➢ If the price is less than 100, there will be a 5% discount.
➢ If the price is negative, there will be no discount
➢ Sample Input: price = 250
➢ Sample Output: price = 20 """
price=int(input("enter price "))
if price >=300 :
    price=((30*price)/100)
elif price >=200 :
       price=((20*price)/100)
elif price >=100 :
       price=((10*price)/100)
elif price >0 :
     price=((5*price)/100)
else:
    price=price 
print(price)        