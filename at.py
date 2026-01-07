total_classes = int(input("Enter total classes: "))
class_attended = int(input("Enter no.of classes attended: "))

attendance_percentage = (class_attended/total_classes)*100

print(f"Attendance percentage: {attendance_percentage}%")

if attendance_percentage < 75:
    print("Not Eligible")
    additional_classes = total_classes - class_attended - 20
    print(f"Additional classes required: {additional_classes}")
else:
    print("Eligible")

