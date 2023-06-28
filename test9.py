#def discounter(price):
   # discount = price * 0.1
  #  discounted = price - discount
 #   return discounted

#price = 100
#finalprice = discounter(price)
#print(finalprice)



def discounter(price, discount):
    discounted = price - (price * discount)
    return discounted

g = float(input("type price:"))

x = float(input("discount:"))

i= discounter(g , x/100)

print(i,"is price with discount!")