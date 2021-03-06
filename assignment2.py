import time
import random
option = random.choice(["wicked fairie", "pirate", "dragon", "troll",
                        "gorgon"])


def decide(item, option):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    respons = input("(Please enter 1 or 2.)")
    if respons == "1":
        approach_the_house(item, option)
    elif respons == "2":
        Road_to_cave(item, option)
    elif respons != "1" or "2":
        print("(Please enter 1 or 2.)")
        decide(item, option)


def play_again():
    response = input("Would you like to play again? (y/n)")
    if response == "y":
        print_pause("\n\n\nExcellent! Restarting the game ...\n\n\n")
        play_game()
    elif response == "n":
        print_pause("\n\n\nThanks for playing! See you next time.\n\n\n")
    else:
        play_again()


def print_pause(text):
    print(text)
    time.sleep(0.1)


def Road_to_cave(item, option):
    if "sword" in item:
        print_pause("\nYou peer cautiously into the cave.")
        print_pause("\nYou've been here before, and gotten all"
                    " the good stuff. It's just an empty cave"
                    " now.")
        print_pause("\nYou walk back to the field.\n")
        decide(item, option)
    else:
        print_pause("\nYou peer cautiously into the cave.")
        print_pause("\nIt turns out to be only a very small cave.")
        print_pause("\nYour eye catches a glint of metal behind a "
                    "rock.")
        print_pause("\nYou have found the magical Sword of Ogoroth!")
        print_pause("\nYou discard your silly old dagger and take "
                    "the sword with you.")
        print_pause("\nYou walk back out to the field.\n")
        item.append("sword")
        decide(item, option)


def run_away(item, option):
    print_pause("You run back into the field. Luckily,\n"
                "you don't seem to have been followed.")
    decide(item, option)


def approach_the_house(item, option):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and\n"
                "out steps  " + option + ".")
    print_pause("Eep! This is  " + option + "'s  house!")
    if "sword" not in item:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.\n")
    print_pause("The dragon attacks you!")
    while True:
        response = input("Would you like to (1) fight or (2)"
                         "run away?")
        if response == "1":
            if "sword" in item:
                print_pause("\nAs the " + option + " moves to attack, "
                            "you unsheath your new sword.")
                print_pause("\nThe Sword of Ogoroth shines brightly in "
                            "your hand as you brace yourself for the "
                            "attack.")
                print_pause("\nBut the " + option + "takes one look at "
                            "your shiny new toy and runs away!")
                print_pause("\nYou have rid the town of the " + option +
                            ". You are victorious!\n")
            else:
                print_pause("\nYou do your best...")
                print_pause("but your dagger is no match for the "
                            + option + ".")
                print_pause("\nYou have been defeated!\n")
            play_again()
            break

        if response == "2":
            print_pause("\nYou run back into the field. "
                        "\nLuckily, you don't seem to have been "
                        "followed.\n")
            decide(item, option)
            break


def defeat():
    print_pause("You do your best.")
    print_pause("but your dagger is no match for the pirate.")
    print_pause("You have been defeated!")
    play_again()


def intro(item, option):
    print_pause("You find yourself standing in an open field,\n"
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a" + option + " is somewhere around\n"
                " here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) \n"
                "dagger.")
    decide(item, option)


def play_game():
    item = []
    intro(item, option)
    decide(item, option)


play_game()
