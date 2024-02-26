k = []
punctuation = ".,?!\n"
with open(f"function_b.txt", "r") as file:
    for line in file:
        line = line.lower().split(" ")
        for words in line:
            for char in words:
                for p in punctuation:
                    if p == char:
                        words = words.replace(char, "")
            if words.startswith("b") and len(words) == 3:
                k.append(words)
print(k)



