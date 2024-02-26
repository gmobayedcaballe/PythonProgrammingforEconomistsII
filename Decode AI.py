def decode_line(line):
    vowels = "aeiouAEIOU"
    count_vowels = sum(1 for char in line if char in vowels)
    return chr(ord('a') + count_vowels - 1) if count_vowels else " "

decoded_message = ""
with open("secret.txt", "r") as file:
    for line in file:
        decoded_message += decode_line(line)

print("Decoded message:", decoded_message)

