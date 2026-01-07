total = 0
cart = []
prices = []
quantity = []
while True:
    choice = input("Enter the item you want to buy: ").lower()
    if choice == "q":
        break
    cart.append(choice)
    price = float(input("Enter the price: "))

    quantity = int(input("Enter the quantity: "))
    cost = quantity*price
    prices.append(cost)


print("-----YOUR CART-----")
for thing in cart:
    print(thing)
print("------------------")

for price in prices:
    total += price

print(f"Total amount: {total}")
discount = int(input("Enter discount: "))

print(f"Discount: {discount}")
total = total - discount
print(f"Final amount: {total}")