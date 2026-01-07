expenses = {}
total = 0

while True:
    category = input("Enter the category(Food, travel, etc): ").lower()
    if category == "q":
        break
    expense = int(input("Enter the expense: "))
    
    if category in expenses:
        expenses[category] += expense
    else:
        expenses[category] = expense
    
    total += expense

print(f"Total expenditure: {total}")

if expenses:
    max_key = max(expenses, key=expenses.get)
    print(f"Highest spending category: {max_key} with value {expenses[max_key]}")
else:
    print("No expenses added.")
