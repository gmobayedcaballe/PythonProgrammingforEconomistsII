def greet():
    """
    This function prints "Hello, World!"
    :return:
    """
    print("Hello, World!")
greet()

def sum_3_numbers(a,b,c=0): # if we add c = 0 if the user doesn't input a value for c the function assumes c = 0
    """
    This function sums 3 numbers
    :param a: first nº
    :param b: second nº
    :param c: third nº
    :return: the sum of the 3 numbers
    """
    return a + b +c

print(sum_3_numbers(1,2, 3))
print(sum_3_numbers(c = 3,b = 2,a = 1))

def read_3_numbers ():
    """
    This function reads 3 numbers from the user
    :return: 3 numbers
    """
    a = int(input("Enter the first nº"))
    b = int(input("Enter the second nº"))
    c = int(input("Enter the third nº"))
    return print(a,b,c)

