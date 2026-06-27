ram = int(input("Enter Ram's age: "))
shyam = int(input("Enter Shyam's age: "))
mohan = int(input("Enter Mohan's age: "))
prit = int(input("Enter Prit's age: "))

if ram > shyam and ram > mohan and ram > prit:
    print("Ram is elder")
elif shyam > ram and shyam > mohan and shyam > prit:
    print("Shyam is elder")
elif mohan > ram and mohan > shyam and mohan > prit:
    print("Mohan is elder")
elif prit > ram and prit > shyam and prit > mohan:
    print("Prit is elder")
else:
    print("Two or more persons have the same highest age")