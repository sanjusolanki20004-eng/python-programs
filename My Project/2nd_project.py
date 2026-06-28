# product list
prices =[]
n = int(input("enter your product in list :"))

for i in range(n):
    price = float(input(f"Enter your prices of your product {i+1}: "))
    prices.append(price)

total = sum(prices)
print("prices of your product:", prices)
print("Total amount =", total)    
    
    
 
    
