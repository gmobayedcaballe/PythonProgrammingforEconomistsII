#Anticipating & dealing w/ exceptions

try:
    age1 = int(input("What's your age, player 1?"))
    age2 = int(input("What's your age, player 2?"))
    res = age1/age2
except ValueError:
    print("I am sorry, but that is not a valid number")
except ZeroDivisionError:
    print("I am sorry, but you cannot divide by zero")
except:
    print("I am sorry, but something went wrong")
else: #If there is no except what the progran should do
    print(f"Player 1 is older than player 2 by a factor of {res}")
finally:
    print("Thank you for playing. If you received an error please run the game again.")

