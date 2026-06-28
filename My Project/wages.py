hours = int(input("Enter working hours: "))

if hours == 8:
    wage = 250

elif hours > 8 and hours <= 10:
    wage = 250 + (hours - 8) * 50

elif hours > 10 and hours <= 12:
    wage = 250 + (2 * 50) + (hours - 10) * 75

elif hours > 12 and hours <= 14:
    wage = 250 + (2 * 50) + (2 * 75) + (hours - 12) * 100

else:
    print("Invalid working hour")
    exit()

print("Daily Wage =", wage)
