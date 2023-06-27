def discounter(price):
    discount = price * 0.1
    discounted = price - discount
    return discounted

price = 100
finalprice = discounter(price)
print(finalprice)