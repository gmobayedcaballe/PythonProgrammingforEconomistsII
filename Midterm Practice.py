def print_b_words(file_name):
    """
    :param file_name:
    :return:
    """
    punctuation = ",.!?'\n"
    with open(file_name, "r") as file:
        for line in file:
         words = line.split(" ")
            for word in words:
                if (word.startswith("b") or word.startswith("B")) and len(word) == 3:
                    print(word)

print(print_b_words("x_files.txt"))

#Not working

