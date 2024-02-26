a = [1,3,5,9,6,7,8]
print(a)
# A list, unlike strings, are mutable, thus their content can be changed a posteriori

a[1] = 8 # changes the item in the nth pos. starting at 0
print(a)

#Slicing a list, works like w/ strings

print(a[0:4])

print(len(a)) # However, positions go from 0 to n-1

t = a.pop(1)
print(a)
print(t)

# a.append
