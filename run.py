from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Fore.MAGENTA + 'some red text')
print(Fore.YELLOW + 'some red text')
print(Fore.BLUE + 'some red text')

#Function to ask the player if they want to play again
def replay_game():
    """
    Function to get the player back into the game
    if they want to play again, and if not take them
    back to the begining
    """

    replay_game_answer = input(Fore.BLUE + "Would you like to play the game again? (yes/no): ").lower().strip()
    if replay_game_answer == "yes":
        game_intro()
    elif replay_game_answer == "no":
        print(Fore.YELLOW + "Thank You for playing the game, have a lovely day....")
    else replay_game_answer():
        print(Fore.RED + "invalid option, try again")


#Function to end the game at the first point
def end_one():
    """
    Function for the Player to end the game
    at the first point in the game
    """
    print("End one activated")


#Function to end the game at the first point
def end_two():
    """
    Function for the Player to end the game
    at the second point in the game
    """
    print("End two activated")

#Function to end the game at the first point
def end_three():
    """
    Function for the Player to end the game
    at the third point in the game
    """
    print("End three activated")


#Function to end the game at the first point
def end_four():
    """
    Function for the Player to end the game
    at the fourth point in the game
    """
    print("End four activated")


#Function to end the game at the first point
def final_end():
    """
    Function for the Player to end the game
    at the final point in the game
    """
    print("Final End activated")

options = ("invalid option, try again", "You have selected - ", "Option a ", "Option b ", "Option c ")

#Question number ten
def leave_in_a_hurry():
    """
    Function to have the Player leave quickly scared
    this would then have the game end
    """
    print(Fore.BLUE + "Your out of the ship, so scared with whats just happened.\n")
    question_ten = input(Fore.MAGENTA + "What do you do?:\n a: Catch your breath and get up the\ncourage to follow the sound again?\nb: Leave the ship and go home?\n").lower().strip()

    if question_ten == "a":
        print((options[1, 2]))
        follow_the_sound()
    elif question_ten == "b":
        print(Fore.YELLOW + "You have selected - Option b - Leave the ship and go home?")
        end_three()
    else:
        print(Fore.RED + "invalid option, try again")
        leave_in_a_hurry()    

#Question number eleven
def door_open():
    """
    Function for the Player to open the door inside the 
    ship to find the sound
    """
    print(Fore.BLUE + "You slowly open the door, trying hard to not see what is there.\nThen the final part of door opens fast.\nYou see a figure...\n")
    
    final_end = input(Fore.MAGENTA + "Type in sound, to see what happens next?").lower().strip()

    while final_end == "sound":
        print(Fore.BLUE + "With a scream, you are startled awake.\nYou slowly start to realise that you where asleep the whole time.\n The dream felt so real.\n")
        final_end()
    else:
        print(Fore.RED + "Wrong word, type sound.\n")
        final_end


#Question number six
def inside_the_ship():
    """
    Function to have you move into the ship and carry on the 
    exploration
    """
    print(Fore.BLUE + "Your eyes start to adjust to the dark inside the ship.\n Just then you hear a metal on metal banging noise.\n")
    
    question_six = input(Fore.MAGENTA + "What do you do?:\n a: Follow the sound to find the source?\nb: Go back through the hatch and onto\nthe upperdeck?\n").lower().strip()

    if question_six == "a":
        print(Fore.YELLOW + "You have selected - Option a - Follow the sound to find the source?\n")
        follow_the_sound()
    elif question_six == "b":
        print(Fore.YELLOW + "You have selected - Option b - Go back through the hatch and onto the upperdeck?")
        walking_the_upperdeck()
    else:
        print(Fore.RED + "invalid option, try again")
        inside_the_ship()



#Question number seven
def walking_the_upperdeck():
    """
    Function to have the Player walk around the upperdeck
    and find a potential way into the ship
    """
    print(Fore.BLUE + "Whilst walking around the upper deck.\nYou see a ghost like figure.\n")
    
    question_seven = input(Fore.MAGENTA + "What do you do?:\n a: Chase the figure to see what its doing?\nb: Get off the ship in quicktime and\ngo home?\n").lower().strip()

    if question_seven == "a":
        print(Fore.YELLOW + "You have selected - Option a - Chase the figure to see what its doing?\n")
        chase_the_figure()
    elif question_seven == "b":
        print(Fore.YELLOW + "You have selected - Option b - Get off the ship in quicktime and go home?")
        end_two()
    else:
        print(Fore.RED + "invalid option, try again")
        walking_the_upperdeck()

#Question number eight
def follow_the_sound():
    """
    Function to have the player follow the sound you can hear
    inside the ship
    """
    print(Fore.BLUE +"Whilst walking down the ships flats,\nthe banging starts to get louder,\nyou start to shake as it gets louder and louder.\n")
    
    question_eight = input(Fore.MAGENTA + "What do you do?:\n a: Open the door to see the source of the sound?\nb: Leave the ship as quick as you can?\n").lower().strip()

    if question_eight == "a":
        print(Fore.YELLOW + "You have selected - Option a - Open the door to see the source of the sound?\n")
        door_open()
    elif question_eight == "b":
        print(Fore.YELLOW + "You have selected - Option b - Leave the ship as quick as you can?")
        leave_in_a_hurry()
    else:
        print(Fore.RED + "invalid option, try again")
        follow_the_sound()

#Question number nine
def chase_the_figure():
    """
    Function to have the play chase the figure you have just seen
    maybe it was a figment of your imagination
    """
    print(Fore.BLUE + "You run after the figure through a door,\ndown some stairs.\nAs you reach the halls of the ship you hear a loud,\nbanging noise, metal on metal banging.\n")
    
    question_nine = input(Fore.MAGENTA + "What do you do?:\n a: Follow the sound?\nb: Leave the ship as quick as you can?\n").lower().strip()

    if question_nine == "a":
        print(Fore.YELLOW + "You have selected - Option a - Follow the sound?\n")
        follow_the_sound()
    elif question_nine == "b":
        print(Fore.YELLOW + "You have selected - Option b - Leave the ship as quick as you can?")
        leave_in_a_hurry()
    else:
        print(Fore.RED + "invalid option, try again")
        chase_the_figure()

#Question one story opener function
def opener_question():
    """
    Function for question one to allow the user to,
    select their first path using an if/elif loop to tell the 
    player what they have selected and get them to the next function
    """

    print(Fore.BLUE + "You spot an abandoned Warship in the sea by your house,\nyou decide to venture towards the ship.\nYou spot there is no Captain or Crew aboard the ship.\n")
    print(Fore.BLUE + "You get in your rowing boat and head towards the Warship.\nYou see a ladder hanging over the side of the ship,\nswaying in the wind.")
    question_one = input(Fore.MAGENTA + "What do you do?:\n a: Climb aboard the ship alone?\nb: Report the ship to the coast guard?\nc: Call your friends to go aboard with you?\n").lower().strip()

    if question_one == "a":
        print(Fore.YELLOW + "You have selected - Option a - Climb aboard the ship alone?\n")
        aboard_the_ship()
    elif question_one == "b":
        print(Fore.YELLOW + "You have selected - Option b - Report the ship to the coast guard?")
        see_a_figure()
    elif question_one == "c":
        print(Fore.YELLOW + "You have selected - Option c - Call your friends to go aboard with you?")
        friends_arrive()

#To get aboard the ship function question two
def aboard_the_ship():
    """
    Function for question two to show the path to,
    aboard the ship
    """
    print(Fore.BLUE + "Now you have climbed up the ladder, onto the Warship.\nYou start to walk around and see an open hatch.\n")
    question_two = input(Fore.MAGENTA + "What do you do?:\n a: Go inside the ship through the hatch?\nb: Close the hatch and carry on walking?\n").lower().strip()

    if question_two == "a":
        print(Fore.YELLOW + "You have selected - Option a - Go inside the ship through the hatch?\n")
        inside_the_ship()
    elif question_two == "b":
        print(Fore.YELLOW + "You have selected - Option b - Close the hatch and carry on walking?")
        walking_the_upperdeck()
    else:
        print(Fore.RED + "invalid option, try again")
        aboard_the_ship()


#Question number three function
def see_a_figure():
    """
    Function for question three to see a figure on the
    ship, this enables you to go back to getting aboard the ship.
    """
    print(Fore.BLUE + "Whilst your drifting around this huge,\nWarship waiting for the Coastguard.\nYou see a figure aboard the Ship.\n")
    question_three = input(Fore.MAGENTA + "What do you do?:\n a: Climb aboard the ship to make sure they are okay?\nb: Take your boat futher away from the Warship?\n").lower().strip()

    if question_three == "a":
        print(Fore.YELLOW + "You have selected - Option a - Climb aboard the ship to make sure they are okay?\n")
        aboard_the_ship()
    elif question_three == "b":
        print(Fore.YELLOW + "You have selected - Option b - Take your boat futher away from the Warship?")
        coastguard()
    else:
        print(Fore.RED + "invalid option, try again")
        see_a_figure()



#Question number four
def friends_arrive():
    """
    Function to have your friends arrive to carry on the 
    explouration of the ship
    """
    print(Fore.BLUE + "Your friends are by your side,\nthis gives you a boost of confidence.\nBrian suggests climbing aboard the Ship.\n")
    question_four = input(Fore.MAGENTA + "What do you do?:\n a: Follow Brian aboard the ship?\nb: Tell them you want to go home?\n").lower().strip()

    if question_four == "a":
        print(Fore.YELLOW + "You have selected - Option a - Climb aboard the ship to make sure they are okay?\n")
        aboard_the_ship()
    elif question_four == "b":
        print(Fore.YELLOW + "You have selected - Option b - Take your boat futher away from the Warship?")
        end_one()
    else:
        print(Fore.RED + "invalid option, try again")
        friends_arrive()

#Question number five
def coastguard():
    """
    Function to have the coastguard assist in seeing the ship,
    to report it and also to find if your allowed to board the ship
    """
    print(Fore.BLUE + "The Coastguard has arrived,\nyou start to tell them about finding the Warship.\nThey tell you that they will check it out.\n")
    question_five = input(Fore.MAGENTA + "What do you do?:\n a: Walk the upperdeck with them?\nb: Tell them you want to go home?\n").lower().strip()

    if question_five == "a":
        print(Fore.YELLOW + "You have selected - Option a - Walk the upperdeck with them?\n")
        walking_the_upperdeck()
    elif question_five == "b":
        print(Fore.YELLOW + "You have selected - Option b - Take your boat futher away from the Warship?")
        end_one()
    else:
        print(Fore.RED + "invalid option, try again")
        coastguard()


#Quit the game function to allow the Player to leave
def quit_game():
    """
    Function to allow the Player to leave the game,
    at multiple points including the menu and during
    game play
    """
    i = "You have decided to Quit the game, Thanks for playing.\n"
    while True:
        print(i)
        game_intro()
    
    print("quit game activated")



#Play game function to start into the questions
def play_game():
    """
    Function for game play to start and push the player
    towards the first question
    """
    print("You have selected Play the Game.\n")
    opener_question()

#Read game function to explain to the Player the backstory of the game
def read_game_story():
    """
    Function for the backstory of the game which once has been printed will
    send the Player back to the menu
    """
    print(Fore.YELLOW + "Warship is a text based game that brings you to the shore line by your house,\nwhen you arrive at the waters edge, you see a World War II Warship.")
    print(Fore.YELLOW + "This ship looks as though it is abandoned, and it sends shivers down your spine.\nYou decide to go towards the vessel to see if its real or your imagination.")
    print(Fore.YELLOW + "When you get to the ship, thr story takes you down various paths and as the story\nunfolds you become, more intrested in what the ship has to offer.")
    menu()


#Opening page for game
def game_intro():
    """
    Function to introduce the player to the game,
    the story opens in 5 lines
    """
    print(Fore.BLUE + "Welcome to Warship, the game where your choices can change your life.\n")
    print(Fore.BLUE + "Warship is designed for you to move through the different paths\n")
    menu()



    #Menu for the Player to select their path
def menu():
    """
    Function to receive the Player path,
    to start the game, learn more about the story,
    or quit the game
    """
    print(Fore.BLUE + "Please select from one of the options below\n")

    #Variable for the Opening Menu
    menu_answer = input(Fore.MAGENTA + "Would you like to:\n A: Start the Game?\n B: Read the backstory to Warship?\n C: Quit the game?\n (A, B or C): ").lower().strip()

    if menu_answer == "a":
        play_game()

    elif menu_answer == "b":
        read_game_story()

    elif menu_answer == "c":
        quit_game()

    else:
        print(Fore.RED + "Invalid Entry, please select the correct input using a, b or c")
        game_intro()



game_intro()



