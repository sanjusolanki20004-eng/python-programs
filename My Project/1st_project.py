# RD Account
name =(input("Enter your name "))
age =int(input("Enter your age "))
if age >= 60:
    print("you are  eligible")
else :
    print("you not eligble")
    
amount = float(input("enter your amoount"))

if amount >=500:
    print("successfully opened your account")
 
else:
    print(" you are not eligible for opening account") 

account = input("Enter your Account Type (Normal/Premium): ")  
if account.lower() == "premium":
    rate = 8
else :  
    rate = 7
      
maturity =amount + (amount* rate * 5)/100
print("--- FD Details---")
print("Name", name) 
print("Age", age)
print("Amount", amount) 
print("Account Type" ,account)
print("FD PERIOD : 5 years")  
print("Maturity Amount :", maturity)    

      