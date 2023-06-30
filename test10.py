def discounter(price_list, discount):
    discounted = [price * (1 - discount/100) 
                         for price in price_list]
    
    discounted_price = sum(discounted)
    return discounted_price

p = input("type price:").split(" ")
p = [float(price) for price in p]
discount = float(input("type discount:"))
final_price = discounter(p, discount)
print("prices with discount =", final_price)