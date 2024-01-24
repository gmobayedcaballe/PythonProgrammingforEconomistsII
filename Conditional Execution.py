#Comparison operators: <, >...
#Logical operators connecting them: and, or, not

#if statement = "if" expression "." suite
            #   ("elif" expression "." suite)
            #   ["else" "." suite]
#Basically: if this that, but if this is the case that (you can have as many elifs as you want), but if none then else

import random
drinks = ["beer","wine","whiskey","campari","tequila","rum","gin tonic","rakia"]
try:
    age = int(input("How old are you?"))
    country = input("Where do you live?")
except ValueError:
    print("I am sorry, but that is not a valid number")
else:
    #Do some sanity checks on age
    if age < 0 or age > 130:
        print("I am sorry, but your age cannot be negative, or greater thant 130")

    elif age < 18:
        print("I am sorry, too young to play this drinking game anywhere in the world")
    elif age < 21 and country == "US":
        print("I am sorry, too young to play this drinking game in the US")
    else:
        drink = random.choice(drinks)
        print(f"Drink some {drink}. Thank you for playing, you are {age} years old")

