import os
from colorama import Fore


def clear():
    """
    Clear function to clear up the terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')


choices = [
    "invalid option, try again",
    "You have selected - Option a - ",
    "You have selected - Option b - ",
    "You have selected - Option c - "]


def replay_game():
    """
    Function to get the player back into the game
    if they want to play again, and if not take them
    back to the beginning
    """
    replay_game_answer = input(
        Fore.BLUE + "Would you like to play the game again? (yes/no): ").lower(
        ).strip()
    if replay_game_answer == "yes":
        game_intro()
    elif replay_game_answer == "no":
        clear()
        print(
            Fore.YELLOW + "Thank You for playing the game, have a lovely day.")
    else:
        print(Fore.RED + choices[0])
        replay_game()


def end_game(result):
    """
    Function for the Player to end the game
    at the all points including the final end game
    """

    if result == 'final':
        print(
            Fore.RED + "YOUR LYING IN BED, SWEATING\nTHE DREAM FELT SO REAL")
    else:
        print(Fore.RED + "You have decided to go home....")
    replay_game()


options = (
    "invalid option, try again",
    "Option a ", "Option b ",
    "Leave the ship and go home?")


def leave_in_a_hurry():
    """
    Function to have the Player leave quickly scared
    this would then have the game end for question ten
    """
    clear()
    print(
        Fore.BLUE + "Your out of the ship,"
        "so scared with whats just happened.")
    question_ten = input(
        Fore.MAGENTA + "\nWhat do you do?:"
        "\na: Catch your breath and get up the"
        "\ncourage to follow the sound again?"
        "\nb: Leave the ship and go home?\n").lower().strip()

    if question_ten == "a":
        print(options[1])
        follow_the_sound()
    elif question_ten == "b":
        print(
            Fore.YELLOW + "You selected - " +
            options[2] + options[3])
        end_game('non final')
    else:
        print(Fore.RED + options[0])
        leave_in_a_hurry()


def door_open():
    """
    Function for the Player to open the door inside the
    ship to find the sound
    """

    print(
        Fore.BLUE +
        "You slowly open the door, trying hard to not see what is there."
        "\nThen the final part of door opens fast.\nYou see a figure...\n")

    final_end_answer = input(
        Fore.MAGENTA + "Type in sound, to see what happens next?").lower(
        ).strip()

    if final_end_answer == "sound":
        print(
            Fore.RED + "With a scream, you are startled awake.\n"
            "You slowly start realising that you where asleep the whole time."
            "\nThe dream felt so real.\n")
        end_game('final')
    else:
        clear()
        print(Fore.RED + "Wrong word, type sound.\n")
        door_open()


def inside_the_ship():
    """
    Function to have you move into the ship and carry on the
    exploration for question six
    """
    clear()
    print(
        Fore.BLUE + "Your eyes start to adjust to the dark inside the ship."
        "\nJust then you hear a metal on metal banging noise.")

    question_six = input(
        Fore.MAGENTA + "\nWhat do you do?:"
        "\na: Follow the sound to find the source?"
        "\nb: Go back through the hatch and onto\nthe upper deck?\n").lower(
        ).strip()

    if question_six == "a":
        print(Fore.YELLOW + "Follow the sound to find the source?\n")
        follow_the_sound()
    elif question_six == "b":
        print(
            Fore.YELLOW + choices[1] +
            "Go back through the hatch and onto the upper deck?")
        walking_the_upperdeck()
    else:
        print(Fore.RED + choices[0])
        inside_the_ship()


def walking_the_upperdeck():
    """
    Function to have the Player walk around the upper-deck
    and find a potential way into the ship question seven
    """
    clear()
    print(
        Fore.BLUE + "Whilst walking around the upper deck."
        "\nYou see a ghost like figure.")

    question_seven = input(
        Fore.MAGENTA + "\nWhat do you do?:"
        "\na: Chase the figure to see what it's doing?"
        "\nb: Get off the ship in quicktime and\ngo home?\n").lower().strip()

    if question_seven == "a":
        print(
            Fore.YELLOW + choices[1] +
            "Chase the figure to see what it's doing?\n")
        chase_the_figure()
    elif question_seven == "b":
        print(
            Fore.YELLOW + choices[2] +
            "Get off the ship in quicktime and go home?")
        end_game('non final')
    else:
        print(Fore.RED + choices[0])
        walking_the_upperdeck()


def follow_the_sound():
    """
    Function to have the player follow the sound you can hear
    inside the ship question eight
    """
    clear()
    print(
        Fore.BLUE +
        "Whilst walking down the ships flats,"
        "\nthe banging starts to get louder,"
        "\nyou start to shake as it gets louder and louder.")

    question_eight = input(
        Fore.MAGENTA + "\nWhat do you do?:"
        "\na: Open the door to see the source of the sound?"
        "\nb: Leave the ship as quick as you can?\n").lower().strip()

    if question_eight == "a":
        print(
            Fore.YELLOW + choices[1] +
            "Open the door to see the source of the sound?\n")
        door_open()
    elif question_eight == "b":
        print(
            Fore.YELLOW + choices[2] +
            "Leave the ship as quick as you can?")
        leave_in_a_hurry()
    else:
        print(Fore.RED + choices[0])
        follow_the_sound()


def chase_the_figure():
    """
    Function to have the play chase the figure you have just seen
    maybe it was a figment of your imagination
    """
    clear()
    print(
        Fore.BLUE + "You run after the figure through a door,"
        "\ndown some stairs."
        "\nAs you reach the halls of the ship you hear a loud,"
        "\nbanging noise, metal on metal banging.")

    question_nine = input(
        Fore.MAGENTA + "\nWhat do you do?:\na: Follow the sound?"
        "\nb: Leave the ship as quick as you can?\n").lower().strip()

    if question_nine == "a":
        print(Fore.YELLOW + choices[1] + "Follow the sound?\n")
        follow_the_sound()
    elif question_nine == "b":
        print(Fore.YELLOW + choices[2] + "Leave the ship as quick as you can?")
        leave_in_a_hurry()
    else:
        print(Fore.RED + choices[0])
        chase_the_figure()


def opener_question():
    """
    Function for question one to allow the user to,
    select their first path using an if/elif loop to tell the
    player what they have selected and get them to the next function
    """
    print(
        Fore.BLUE + "You spot an abandoned Warship in the sea by your house,"
        "\nyou decide to venture towards the ship."
        "\nYou spot there is no Captain or Crew aboard the ship.\n")
    print(
        Fore.BLUE + "You get in your rowing boat and head towards the Warship."
        "\nYou see a ladder hanging over the side of the ship,"
        "\nswaying in the wind.")
    question_one = input(
        Fore.MAGENTA + "\nWhat do you do?:\na: Climb aboard the ship alone?"
        "\nb: Report the ship to the coast guard?"
        "\nc: Call your friends to go aboard with you?\n").lower().strip()

    if question_one == "a":
        print(Fore.YELLOW + choices[1] + "Climb aboard the ship alone?\n")
        aboard_the_ship()
    elif question_one == "b":
        print(
            Fore.YELLOW + choices[2] +
            "Report the ship to the coast guard?")
        clear()
        see_a_figure()
    elif question_one == "c":
        print(
            Fore.YELLOW + choices[3] +
            "Call your friends to go aboard with you?")
        clear()
        friends_arrive()
    else:
        print(Fore.RED + choices[0])
        opener_question()


def aboard_the_ship():
    """
    Function for question two to show the path to,
    aboard the ship question two
    """
    clear()
    print(
        Fore.BLUE + "Now you have climbed up the ladder, onto the Warship."
        "\nYou start to walk around and see an open hatch.")
    question_two = input(
        Fore.MAGENTA + "\nWhat do you do?:"
        "\na: Go inside the ship through the hatch?"
        "\nb: Close the hatch and carry on walking?\n").lower().strip()

    if question_two == "a":
        print(
            Fore.YELLOW + choices[1] +
            "Go inside the ship through the hatch?\n")
        inside_the_ship()
    elif question_two == "b":
        print(
            Fore.YELLOW + choices[2] +
            "Close the hatch and carry on walking?")
        walking_the_upperdeck()
    else:
        print(Fore.RED + choices[0])
        aboard_the_ship()


def see_a_figure():
    """
    Function for question three to see a figure on the
    ship, this enables you to go back to getting aboard the ship
    question three
    """
    print(
        Fore.BLUE + "\nWhilst your drifting around this huge,"
        "\nWarship waiting for the Coastguard."
        "\nYou see a figure aboard the Ship.")
    question_three = input(
        Fore.MAGENTA +
        "\nWhat do you do?:"
        "\na: Climb aboard the ship to make sure they are okay?"
        "\nb: Take your boat further away from the Warship?\n").lower().strip()

    if question_three == "a":
        print(
            Fore.YELLOW + choices[1] +
            "Climb aboard the ship to make sure they are okay?\n")
        aboard_the_ship()
        clear()
    elif question_three == "b":
        print(
            Fore.YELLOW + choices[2] +
            "Take your boat further away from the Warship?")
        coastguard()
    else:
        print(Fore.RED + choices[0])
        see_a_figure()


def friends_arrive():
    """
    Function to have your friends arrive to carry on the
    exploration of the ship question four
    """
    print(
        Fore.BLUE + "\nYour friends are by your side,"
        "\nthis gives you a boost of confidence."
        "\nBrian suggests climbing aboard the Ship.\n")

    question_four = input(
        Fore.MAGENTA + "\nWhat do you do?:"
        "\na: Follow Brian aboard the ship?"
        "\nb: Tell them you want to go home?\n").lower().strip()

    if question_four == "a":
        print(
            Fore.YELLOW + choices[1] +
            "Climb aboard the ship to make sure they are okay?\n")
        aboard_the_ship()
    elif question_four == "b":
        print(
            Fore.YELLOW + choices[2] +
            "Tell them you want to go home?")
        end_game('non final')
    else:
        print(Fore.RED + choices[0])
        friends_arrive()


def coastguard():
    """
    Function to have the coastguard assist in seeing the ship,
    to report it and also to find if your allowed to board the ship
    question five
    """
    print(
        Fore.BLUE + "The Coastguard has arrived,"
        "\nyou start to tell them about finding the Warship."
        "\nThey tell you that they will check it out.")

    question_five = input(
        Fore.MAGENTA + "\nWhat do you do?:"
        "\na: Walk the upper deck with them?"
        "\nb: Tell them you want to go home?\n").lower().strip()

    if question_five == "a":
        print(Fore.YELLOW + choices[1] + "Walk the upper deck with them?\n")
        walking_the_upperdeck()
    elif question_five == "b":
        print(
            Fore.YELLOW + choices[2] + "Tell them you want to go home?")
        end_game('non final')
    else:
        print(Fore.RED + choices[0])
        coastguard()


def quit_game():
    """
    Function to allow the Player to leave the game,
    at multiple points including the menu and during
    game play
    """
    print(
        Fore.RED + "You have decided to Quit the game, Thanks for playing.\n")


def play_game():
    """
    Function for game play to start and push the player
    towards the first question
    """
    print(Fore.YELLOW + "You have selected Play the Game.\n")
    opener_question()


def read_game_story():
    """
    Function for the backstory of the game which once has been printed will
    send the Player back to the menu
    """
    clear()
    print(
        Fore.YELLOW + "Warship is a text based game that brings you to, "
        "the shore line by your house,\n"
        "when you arrive at the waters edge,"
        "you see a World War II Warship.\n")

    print(
        Fore.YELLOW + "This ship looks as though it is abandoned, "
        "and it sends shivers down your spine.\nYou decide to go "
        "towards the vessel to see if its real or your imagination.\n")

    print(
        Fore.YELLOW + "When you get to the ship, "
        "the story takes you down various paths and as the story\n"
        "unfolds you become, more interested in what the ship has to offer.\n")
    menu()


def game_intro():
    """
    Function to introduce the player to the game,
    the story opens in 5 lines
    """
    clear()
    print(
        Fore.BLUE + "Welcome to Warship,"
        "the game where your choices can change your life.\n")
    print(
        Fore.BLUE +
        "Warship is designed for you to move through the different paths\n")
    menu()


def menu():
    """
    Function to receive the Player path,
    to start the game, learn more about the story,
    or quit the game
    """

    print(Fore.BLUE + "Please select from one of the options below")

    # Variable for the Opening Menu
    menu_answer = input(
        Fore.MAGENTA + "\nWould you like to:"
        "\na: Start the Game?"
        "\nb: Read the backstory to Warship?"
        "\nc: Quit the game?\n(a, b or c): \n").lower().strip()

    if menu_answer == "a":
        play_game()

    elif menu_answer == "b":
        read_game_story()

    elif menu_answer == "c":
        quit_game()
    else:
        print(
            Fore.RED + "Invalid Entry, please select the correct input using"
            "a, b or c\n")
        menu()


game_intro()
