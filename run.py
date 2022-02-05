
#Question one story opener function
def opener_question():
    """
    Function for question one to allow the user to,
    select their first path
    """

    print("You spot an abandoned Warship in the sea by your house,\nyou decide to venture towards the ship.\nYou spot there is no Captain or Crew aboard the ship.\n")
    print("You get in your rowing boat and head towards the Warship.\nYou see a ladder hanging over the side of the ship,\nswaying in the wind.")
    question_one = input("What do you do?:\n a: Climb aboard the ship alone?\nb: Report the ship to the coast guard?\nc: Call your friends to go abouard with you?\n").lower().strip()

    if question_one == "a":
        print("You have selected - Option a - Climb aboard the ship alone?\n")
        aboard_the_ship()
    elif question_one == "b":
        print("You have selected - Option b - Report the ship to the coast guard?")
        see_a_figure()
    elif question_one == "c":
        print("You have selected - Option c - Call your friends to go abouard with you?")
        friends_arrive()

#To get aboard the ship function question two
def aboard_the_ship():
    """
    Function for question two to show the path to,
    aboard the ship
    """
    print("go aboard the ship")


#Question number three function
def see_a_figure():
    """
    Function for question three to see a figure on the
    ship
    """
    print("see a figure activated")

#Question number four
def friends_arrive():
    """
    Function to have your friends arrive to carry on the 
    explouration of the ship
    """
    print("friends arrive activated")

#Question number five
def coastguard():
    """
    Function to have the coastguard assist in seeing the ship,
    to report it and also to find if your allowed to board the ship
    """
    print("coastguard activated")


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
    print("Warship is a text based game that brings you to the shore line by your house,\nwhen you arrive at the waters edge, you see a World War II Warship.")
    print("This ship looks as though it is abandoned, and it sends shivers down your spine.\nYou decide to go towards the vessel to see if its real or your imagination.")
    print("When you get to the ship, thr story takes you down various paths and as the story\nunfolds you become, more intrested in what the ship has to offer.")
    print(menu(input("What would you like to do next?")))


#Opening page for game
def game_intro():
    """
    Function to introduce the player to the game,
    the story opens in 5 lines
    """
    print("Welcome to Warship, the game where your choices can change your life.\n")
    print("Warship is designed for you to move through the different paths\n")
    menu()



    #Menu for the Player to select their path
def menu():
    """
    Function to recieve the Player path,
    to start the game, learn more about the story,
    or quit the game
    """
    print("Please select from one of the options below\n")

    #Variable for the Opening Menu
    menu_answer = input("Would you like to:\n A: Start the Game?\n B: Read the backstory to Warship?\n C: Quit the game?\n (A, B or C): ").lower().strip()

    if menu_answer == "a":
        play_game()

    elif menu_answer == "b":
        read_game_story()

    elif menu_answer == "c":
        quit_game()

    else:
        print("Invalid Entry, please select the correct input using a, b or c")
        game_intro()



game_intro()








    




#Question number six
def inside_the_ship():
    """
    Function to have you move into the ship and carry on the 
    exploration
    """

#Question number seven
def walking_the_upperdeck():
    """
    Function to have the Player walk around the upperdeck
    and find a potentional way into the ship
    """

#Question number eight
def follow_the_sound():
    """
    Function to have the player follow the sound you can hear
    inside the ship
    """

#Question number nine
def chase_the_figure():
    """
    Function to have the play chase the figure you have just seen
    maybe it was a figment of your imagination
    """

#Question number ten
def leave_in_a_hurry():
    """
    Function to have the Player leave quickly scared 
    this would then have the game end
    """

#Question nunber eleven
def door_open():
    """
    Function for the Player to open the door inside the 
    ship to find the sound
    """

#Function to end the game at the first point
def end_one():
    """
    Function for the Player to end the game
    at the first point in the game
    """

#Function to end the game at the first point
def end_two():
    """
    Function for the Player to end the game
    at the second point in the game
    """

#Function to end the game at the first point
def end_three():
    """
    Function for the Player to end the game
    at the third point in the game
    """

#Function to end the game at the first point
def end_four():
    """
    Function for the Player to end the game
    at the fourth point in the game
    """

#Function to end the game at the first point
def final_end():
    """
    Function for the Player to end the game
    at the final point in the game
    """

