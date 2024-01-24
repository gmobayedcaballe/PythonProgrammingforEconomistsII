#Assign vars. w/ "="
#type() to check the type of the var.

#Getting input: input([prompt])
name = input("What's your name?")
age = input("How old are you?")
age = int(age) #age has to be converted to an integer b/c it is previously a string
birth_year = 2023 - age

print(f"You name is {name}, you are {age} years old so you were born in {birth_year}!")
#Have to add f at the start to allow to insert the variables

#Anticipating & dealing w/ exceptions




