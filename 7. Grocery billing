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
discount_amount = int(input("Enter discount: "))
discount=total*(discount_amount/100)
final_total=total-discount
print(f"Discount: {discount}%")
print(f"Final amount: {final_total}")
