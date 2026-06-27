price = float(input("Enter the Book Price :" ))

if price > 500 :
    discount = price * 0.20
    
else :
    discount = price * 0.10
    
    
final_price = price -discount


print ("book price :",price)
print("discount :",discount)
print("final_price :",final_price)
