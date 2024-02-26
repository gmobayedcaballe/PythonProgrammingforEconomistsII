def username():
    """
    This function creates a usernames based on input names.
    :return:
    """

    name = input("What is your  name? ")
    while name.isdigit() == True:
        name = input("What is your name? Please don't include numbers ")
    surname = input("What is your surname?")
    while surname.isdigit() == True:
        surname = input("What is your surname? Please don't include numbers ")
    a = list(surname.split(" "))
    k = []
    print(a)
    if len(a) == 1:
        print(f"Your username is {name[0].lower()+surname.lower()}")
    else:
        for i in a:
            if i != a[-1]:
               j = i[0]
               k.append(j)
            else:
                l = i
                k.append(l)

        initials = "".join(k)
        print(f"Your username is {name[0]+initials}")


username()




