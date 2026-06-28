income = float(input("Enter a income of person (in Lakh): "))

if income <= 1200000 :
    tax = 0

elif income <= 1600000 :
    tax = income *0.5 / 100
    

elif income <= 2000000 :
    tax = income * 0.10 / 100

elif income <= 2400000 :
    tax = income * 0.15 / 100
    
else :
 tax = income * 0.20 /100
 
print ("income tax =",tax)




 
