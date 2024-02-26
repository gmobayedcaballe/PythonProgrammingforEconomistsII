f = open("x_files.txt", "a")
while True:
    line = input("give me some text to write in the file ")
    if line.lower() == "stop":
        break
    f.write(line + "\n")

# we need to close the file at the end

f.close()