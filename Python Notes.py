# Handling Errors

# Try & Except: runs the code in try and if there's an error runs the code in except
# Some errors can be overcome with other code (e.g. while), without forcing the program to stop
# You can use except for different errors (e.g., except ValueError)
# Can be combined with else statement at the end: else is executed if no error occurs

# Break & Continue: Break statement exits the loop, continue skips and restarts the loop

# Range() an interval range([,)) range(start, end (not included), step)

# Important string commands: len(); in operator (e.g. "ban" in "banana"); s.replace(eliminate, replace with); s.split(); s.find()

#Methods: dir(); help(object.method) for a brief description;)

# Template function, e.g.:
# template = "Today is %s"
# print(template %"Tuesday")
# The letter after the % indicates the conversion type: %s = string; %d = integer; %g = float; %x = hexadecimal

string = input("Give me a string ")
string = string.lower()
punctuation = ".?!,;"

for letter in string:                           # For every letter in the string its going to iterate through every p in punctuation and find
    for p in punctuation:                       # if any p matches and replace that letter w/ nothing. It will only go to the next letter once it has checked if any p
        if letter == p:                         # matches the letter
            string = string.replace(p, "")
print(string)
if string == string[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

#Files

# open("file name", "opening method"): can be opened as r – read (default), w – write, x – exclusive creation,
# a – append, b – binary, t – text (default), + – update (read + write)
# We might have to read the file name depending on the program we are trying to code (w/ read()). The file can be assigned
# to an object

# If you want to write into a file, you must first open the file with either "w" or "a", however, "w" will always start
# with an empty file, i.e., it will rewrite it, while a will simply append it. Then you can use .write() to write into the file
# if you want to move to the next line .write(/n)

# Functions

# def name_of_function(optional arguments)
# if the function takes arguments, when called they will have to be specified within the brackets, e.g.:
def greet(name):
    """
    Input: none
    This function just prints "hello, <name> "
    """
    print('Hello,', str(name).capitalize())

greet("james")

#The parameters can be bind to a value, avoiding them having to be in order, e.g.:
# function(t1,t2,t3) when called can be written as function(t2 = y, t1 = x, t3 = z) instead of
# function(x,y,z)
# add a return to enable the value to be used further, o/w Python will return "None". For instance, if you try to assign the outcome
# of a function to an object but do not specify a return in the function it the object will be assigned "None"
# You can call functions within functions

# Lists

# append()
# extend(): to append another list at the end
# sort(): to sort from highest to lowest value
#.pop can be used to delete values
#del object[]
