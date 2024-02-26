import random

n = input("How many random integers would you like to add? ")
n = int(n)
a = input("What would be the lower bound of the random integers you would like to add (inclusive)? ")
a = int(a)
b = input("What would be the upper bound of the random integers you would like to add (inclusive)? ")
b = int(b)
k = []
for i in range(1,n+1):
    number = random.randint(a,b)
    print(number)
    k.append(number)
final_sum = sum(k)
print(final_sum)



