string = input("Please give me a string ")
k = 0
while len(string)-k-1 >= 0:
    print(string[len(string)-1-k])
    k += 1
