# Create a function in Python that accepts two parameters.
# The first should be the full price of an item as an integer.
# The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has
# been applied. For example, if the price is 100 and the discount is 20,
# the function should return 80.

full_price = int(input("Enter the Value of the Item's Full Price: "))
dis_price = int(input("Enter the value of the discounted price: "))

def price_of_item(full_price,dis_price):
    price_after_discount = full_price - dis_price
    return price_after_discount

print(price_of_item(full_price,dis_price))

# according to chatgpt:
#full_price = int(input("Enter the Value of the Item's Full Price: "))
#dis_percentage = int(input("Enter the value of the discounted percentage: "))

#def price_of_item(full_price,dis_percentage):
#    dis_amount = full_price * (dis_percentage/100)
#    print(dis_amount)
#    dis_price = full_price - dis_amount
#    return int(dis_price)

#print(price_of_item(full_price,dis_percentage))