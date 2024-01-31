#To extract a letter object name[]
#Use of operators "+"
hi = "Hello"
bye = "Bye"
print(hi+bye)
print(hi + " " + bye)

#*
print(3*"abc ")

#len() to obtain the length of a string
print(len(hi))

#for
for letter in hi:
    print(letter)

#Slicing
base = "abcdefgnklsncnioenifnsif"

print("here are some slices")
print(base[0:3]) #Includes the beginning, excludes the end character
print(base[4:]) #All the way from the end
print(base[:4]) #All the way from the beginning
print(base[5:15:3]) #Every third character from the 5th to the 15th
print(base[::-1]) #The whole string backwards

#Strings can be compared with "==", ">", "<" - case matters. The value assigned to a letter ascends as the alphabet moves on, and upercase letters are smaller than lower case letters
#The "in" operator takes two strings and returns True if the first is a substring of the second
print("abc" in base)

#String methods can be found through dir() - the available methods are closely related to the data type of an object
#The help() function can be used to get a short description of a method. E.g.:
help(base.lower)
