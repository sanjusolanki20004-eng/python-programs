num = int(input("Enter a number :"))

fact = 1
while num > 0:
    fact *= num
    num -= 1
print(f"the factorial is given number {fact}")