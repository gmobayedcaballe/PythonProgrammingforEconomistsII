import math
num = input("Please give me a number")
while num.isdigit() == False:
    num = input("Please give me a number")
num = float()
print(f"The square root of this number is {math.sqrt(num)}")