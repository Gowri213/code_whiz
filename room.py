total_seats = int(input("Enter the total no of seats: "))
seating_arrangement = []
count = 1

while count <= total_seats:
    name = input("Enter name: ")
    dept = input("Enter department: ").upper()
    seating_arrangement.append((count, name, dept))
    count += 1

for seat in seating_arrangement:
    print(f"Seat {seat[0]} {seat[1]} {seat[2]}")
