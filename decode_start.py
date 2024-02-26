alphabet = " abcdefghijklmnopqrstuvwxyz"
vowel = "aeiou"
vowel_count = 0
v_line = []
with open("secret.txt", "r") as file:
    for line in file:
        for letter in line:
            for v in vowel:
                if letter == v:
                    vowel_count += 1
        v_line.append(vowel_count)
        vowel_count = 0

print(v_line)
decoded_message = []
for item in v_line:
    j = alphabet[item]
    decoded_message.append(j)

decoded_message = "".join(decoded_message)
print(decoded_message)


