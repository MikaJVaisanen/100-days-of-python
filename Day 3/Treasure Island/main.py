print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice = input("You stand at a crossroad. Will you go left or right? ")
choice = choice.lower()

if choice == "left":
    choice = input("You arrive at the edge of a gloomy lake. Will you wait for a boat or swim? ")
    choice = choice.lower()

    if choice == "wait":
        choice = input("You arrive at a room with 3 doors(red, yellow, blue). Which do you choose? ")
        choice = choice.lower()

        if choice == "red":
            print("You fell into a fiery pit. Game over!")
        elif choice == "yellow":
            print("Congratulations! You found the treasure!")
        elif choice == "blue":
            print("A pack of hungry beasts ate you. Game over!")
        else:
            print("You made an incorrect choice. Game over!")

    elif choice == "swim":
        print("You attempted to cross the lake by swimming, but drowned. Game over!")
    else:
        print("You made an incorrect choice. Game over!")

elif choice == "right":
    print("You tripped, and fell of a cliff. Game over!")
else:
    print("You made an incorrect choice. Game over!")