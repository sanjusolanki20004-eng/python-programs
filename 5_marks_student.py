subject = ("hindi", "english", "maths", "science", "social science")
marks = [
    int(input("Enter marks for hindi : ")),
    int(input("Enter marks for english : ")),
    int(input("Enter marks for maths : ")),
    int(input("Enter marks for science : ")),
    int(input("Enter marks for social science : "))
]

total_marks = sum(marks)
percentage = (total_marks / 500) * 100
average_marks = total_marks / len(marks)

print("Total marks =", total_marks)
print("Percentage =", percentage)
print("Average marks =", average_marks)