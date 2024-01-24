#While: "while" expression "." suite
    #   ["else" "." suite]

import random
lives = 3
while lives: #This is equal to lives > 0 b/c any number not 0 is true
    print(f"You have {lives} lives left")
    dice_roll = random.randint(1,6)
    if dice_roll == 6:
        print("You rolled a 6, you win")
        break
    elif dice_roll == 1:
        print(f"You gained a life")
        lives+=1
  #else is not needed here
        print(f"You rolled a {dice_roll} try again")
        lives -= 1


if lives == 0:
    print("You lost all your lives, game over")

#break: take me out
#continue: take me to the beginning

#for statement = "for" target_list "in" expression_list "." suite
            #  ["else" "." suite]