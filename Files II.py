print("Here will be the contents of the file:")
num_aliens = 0
with open("x_files.txt", "r") as f:
    # Inside here (this indentation) the f file is open for reading
    # print(f.read())
    for line in f:
        num_aliens += line.lower().count("alien")

# Once you're out, the file is closed
print(f"the word alien shows up {num_aliens} times in the fileº")