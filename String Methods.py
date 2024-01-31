text = "abcdefg"
print(dir(text))
help(text.isidentifier)
print(text.isidentifier()) #is abcdefg a valid identifier?

#count

print(text.count("a"))
print(text.replace("a","!!!"))
print("ananananananananana".find("ana",1))
print("bbbabbababbabababbabababbb".split("a"))
print("this is a sentence and I want the words".split(" "))

sentence = "Hello, kind-sir, how may I be of service today?"
punctuation = ".,;!?-"
#Santitize the sentence
for p in punctuation:
    sentence = sentence.replace(p, " ") #Replace punctuation with space to avoid the kindsir problem
print(sentence)
sentence = sentence.replace("  "," ")
#Split the sentence into words
words = sentence.split(" ")
print(words)
