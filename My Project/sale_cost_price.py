# Sale and Cost Price Program

cost_price = float(input("Enter your cost price: "))
sales_price = float(input("Enter your sales price: "))

if sales_price > cost_price:
    profit = sales_price - cost_price
    print(f"The owner made a profit of {profit}")

elif cost_price > sales_price:
    loss = cost_price - sales_price
    print(f"The owner made a loss of {loss}")

else:
    print("No profit, No loss")