expenses = []
ls = []
total = 0
while True:
    category = input("Enter the category(Food, travel, etc): ").lower()
    if category == "q":
        break
    expense = int(input("Enter the expense: "))
    
    ls.append(category)

    expenses.append(expense)

for thing in ls:
    print(thing)
for expense in expenses:
    print(expense)

for expense in expenses:
    total += expense

print(f"Total expenditure: {total}")
print("Highest spending category: ")
print(max(expenses))