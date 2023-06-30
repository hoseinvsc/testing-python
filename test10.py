def discounter(price_list, discount):
    discounted = [price * (1 - discount/100) 
                         for price in price_list]
    
    discounted_price = sum(discounted)
    return discounted_price

prices = input("type price:").split(".")

prices = [float(price) for price in prices]

discount = float(input("type discount:"))

final_price = discounter(prices, discount)

print("prices with discount=", final_price)