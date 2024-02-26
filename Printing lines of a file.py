with open("x_files.txt", "r") as file:
    for line in file:
        print(line.rstrip()) #with .rstrip we remove the whitespace