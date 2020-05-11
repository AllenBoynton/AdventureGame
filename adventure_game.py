import time
import random


def print_pause(message, pause):
    print(message)
    time.sleep(pause)


def intro(enemies, random_enemy):
    print_pause("\nYou find yourself in a clearing atop a "
                "heavily wooded mountain.", 5)
    random_enemy.append(random.choice(enemies))

    print_pause(f"You have heard stories of a {random_enemy[0]} "
                "that roams the mountain!", 5)
    print_pause("West of you is a creepy cabin with smoke coming "
                "from the chimney.", 4)
    print_pause("North is an overgrown trail that goes deep "
                "into the dark, wooded forest.", 5)
    print_pause("All you carry is your trusty pocket-knife.", 2)
    print_pause("You have come in search of the sacred, "
                "legendary weapon!", 4)


def valid_input(prompt, option1, option2, option3):
    while True:
        response = input(prompt)
        if option1 in response:
            break
        elif option2 in response:
            break
        elif option3 in response:
            break
        else:
            print_pause("That is not a valid choice.", 2)
    return response


def choose_direction(weapons, random_enemy, random_weapon):
    print_pause("\nEnter 1 to head towards the creepy cabin.", 1)
    print_pause("Enter 2 to start down the dark trail.", 1)
    print_pause("Enter 3 to go back to the clearing.", 1)
    print_pause("Which way do you want to go?", 1)
    response = valid_input("(Please enter 1 or 2 or 3)\n", "1", "2", "3")
    if "1" in response:
        cabin(weapons, random_enemy, random_weapon)
    elif "2" in response:
        trail(weapons, random_enemy, random_weapon)
    elif "3" in response:
        clearing(weapons, random_enemy, random_weapon)
    choose_direction(weapons, random_enemy, random_weapon)


def choose_status(weapons, random_enemy, random_weapon):
    response = valid_input("\nWould you like to (1) FIGHT or (2) RUN "
                           "AWAY or (3) HIDE?\n", "1", "2", "3")
    if "1" in response:
        fight(random_enemy, random_weapon)
    elif "2" in response:
        run(weapons, random_enemy, random_weapon)
    elif "3" in response:
        hide(weapons, random_enemy, random_weapon)
    response2 = input("Would you like to play again? (Y/N)\n")
    if "y" in response2.lower():
        print_pause("Excellent! Restarting the game ...\n", 2)
        random_enemy.clear()
        random_weapon.clear()
        play_game()
    elif "n" in response2.lower():
        print_pause("\nThanks for playing! See you next time.\n", 2)
        quit()
    else:
        print_pause("That is not a valid choice.", 1)
        choose_status(weapons, random_enemy, random_weapon)


def fight(random_enemy, random_weapon):
    if len(random_weapon) == 0:
        print_pause("You do your best...", 3)
        print_pause("but your measley knife is no match for the "
                    f"{random_enemy[0]}...", 4)
        print_pause("You have been defeated!\n", 2)
        print_pause("GAME OVER\n", 2)
    else:
        print_pause(f"As the {random_enemy[0]} moves to attack, "
                    "you unsheath your legendary weapon.", 4)
        print_pause(f"The {random_weapon[0]} is too much for the "
                    f"{random_enemy[0]} and after it struggles...", 4)
        print_pause(f"the {random_enemy[0]} runs away!", 2)
        print_pause(f"You have defeated the {random_enemy[0]} with "
                    f"the help from your legendary {random_weapon[0]}!!\n", 4)
        print_pause("YOU WIN!!!\n", 2)


def run(weapons, random_enemy, random_weapon):
    print_pause("You feel frozen to the ground.", 2)
    print_pause("You finally snap out of it and you RUN...", 3)
    print_pause(f"You run back into the clearing. The {random_enemy[0]} "
                "is nowhere to be seen.", 4)
    choose_direction(weapons, random_enemy, random_weapon)


def hide(weapons, random_enemy, random_weapon):
    print_pause("You quickly hide behind the nearest tree.", 2)
    if len(random_weapon) == 0:
        print_pause(f"As you anxiously and quietly hide...", 3)
        print_pause(f"the {random_enemy[0]} runs by you and continues "
                    "looking until it returns back to the cabin.", 4)
        print_pause("You need to find the legendary weapon and defeat "
                    f"the {random_enemy[0]}.", 4)
        print_pause("Where are you going to go?", 2)
        choose_direction(weapons, random_enemy, random_weapon)
    else:
        print_pause("As you anxiously and quietly hide...", 4)
        print_pause(f"the {random_enemy[0]} sees your {random_weapon[0]} "
                    "sticking out from behind the tree.", 4)
        print_pause(f"The {random_enemy[0]} attacks you...", 4)
        print_pause("...you have been defeated.", 4)


def cabin(weapons, random_enemy, random_weapon):
    if len(random_weapon) == 0:
        print_pause("You need to check the cabin for a weapon.", 3)
        print_pause("You do not feel good about this with only your "
                    "pocket-knife.", 3)
    else:
        print_pause(f"You're feeling strong with your {random_weapon[0]}!!", 3)
    print_pause("As you approach the cabin...the door opens...", 3)
    print_pause(f"The {random_enemy[0]} starts coming towards you...", 3)
    print_pause(f"The {random_enemy[0]} attacks you!", 4)
    choose_status(weapons, random_enemy, random_weapon)


def trail(weapons, random_enemy, random_weapon):
    print_pause("As you begin your journey down the trail...", 3)
    if len(random_weapon) == 0:
        random_weapon.append(random.choice(weapons))
        print_pause("you see a wooden chest buried just off the path.", 3)
        print_pause(f"You open it to find an all-powerful "
                    f"{random_weapon[0]}.", 4)
        print_pause("You have found the mountain's legendary weapon!", 3)
        print_pause(f"The {random_enemy[0]} knows what you have "
                    "found and is coming after you!!", 4)
        print_pause(f"You need to find the {random_enemy[0]} before it "
                    "finds you!", 3)
    else:
        print_pause(f"you notice is where you found your "
                    "{random_weapon[0]}.", 2)
        print_pause("You need to find another way.", 2)
    print_pause("Now...which way will you go?", 2)
    choose_direction(weapons, random_enemy, random_weapon)


def clearing(weapons, random_enemy, random_weapon):
    print_pause("You turn back to the clearing where your journey "
                "first began.", 3)
    print_pause("As you walk to the end of the clearing, you see "
                "a steep cliff.", 3)
    print_pause("You realize there is nowhere else to go from here.", 3)
    if len(random_weapon) == 0:
        print_pause("You need to check another direction to find "
                    "the legendary weapon.", 4)
        print_pause("You feel as if you are being watched...", 3)
    else:
        print_pause(f"The {random_enemy[0]} attacked you from behind "
                    f"and took your {random_weapon[0]}!", 4)
        random_weapon.clear()
        print_pause("Now all you have is your pocket-knife.", 2)
    print_pause("Time to get out of here!", 2)
    choose_direction(weapons, random_enemy, random_weapon)


def play_game():
    enemies = ["TROLL", "GROTESQUE ORC", "DRAGON", "HOSTILE ALIEN",
               "SINISTER SASQUATCH", "SHADOW DEMON",
               "KILLER ROBOT FROM THE FUTURE"]
    weapons = ["DAGGER", "BATTLE AXE", "LIGHT SABER",
               "ROCKET LAUNCHER", "ASSAULT RIFLE"]
    random_enemy = []
    random_weapon = []
    intro(enemies, random_enemy)
    choose_direction(weapons, random_enemy, random_weapon)


if __name__ == '__main__':
    play_game()
