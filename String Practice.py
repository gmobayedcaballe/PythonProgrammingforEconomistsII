
string = input("Give me a string ")
string = string.lower()
punctuation = ".?!,;"

for letter in string:
    for p in punctuation:
        if letter == p:
            string = string.replace(p, "")
print(string)
if string == string[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
