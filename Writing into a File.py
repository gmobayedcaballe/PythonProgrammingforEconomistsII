
sequence = range(1, 11)

with open("appending.txt", "a") as file:
    for item in sequence:
        line = input(f"This is line {item}, what would you like to write? ")
        file.write(line)
        file.write("\n")