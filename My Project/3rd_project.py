Basic_salery = int(input("Enter your basic salary: "))
hra = Basic_salery * 4/100
da = Basic_salery * 5/100
pf = Basic_salery * 6/100

new_salery = Basic_salery + hra 
new_salery = new_salery + da
new_salery = new_salery - pf

print("hra: ", hra)
print("New Salary: ", new_salery)

print("da: ", da)
print("new Salary: ", new_salery)

print("pf: ", pf)
print("new Salary: ", new_salery)