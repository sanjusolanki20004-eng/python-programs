num = 4512
rev = 0
rev = rev * 10 + num % 10
num = num // 10

rev = rev * 10 + num % 10
num = num // 10

rev = rev * 10 + num % 10
num = num // 10

rev = rev * 10 + num % 10
num = num // 10
print(rev)