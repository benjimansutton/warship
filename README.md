# Warship
​
Warship is a Python terminal game, which runs in the Code Institute mock terminal on Heroku
​
Users answer questions in the game, which will determine the users next path. The game, whilst terminal based is aimed to user the players imagination to envision the scenario.
​
[Here is the live version of my project.](https://warship-app.herokuapp.com/)
​
![Screenshots](documents/testing/screenshots.png)
​
## How to play
​
Warship is a text-based game which have been documented to go back since the 1960's. You can read more about them and their paths through history on [Wikipedia](https://en.wikipedia.org/wiki/Text-based_game).
​
In this game we use multiple choice questions to lead the user down a path either further into the ship, with or without friends.
​
There is no winning or losing, but more the users want to go further into the Warship.
​
## Features
​
### Existing Features
​
* Use of Colorama
    * The use of colorama has been implemented to enable quick and easy viewing if something is inncorrect in RED
    * Using BLUE for the use
* Use of the clear function to clear the users terminal
* 
​
![Random board generation](documents/testing/random.png)
​
* Play against the computer
* Accepts user input
* Maintains scores
​
![Input and scores](documents/testing/input.png)
​
* Input validation and error-checking
    * You cannot enter coordinates outside the size of the grid
    * You must enter numbers
    * You cannot enter the same guess twice
​
![Input validation](documents/testing/errors.png)
​
* Data maintained in class instances
​
### Future Features
​
* Allow player to select the board size and number of ships
* Allow player to position ships themselves
* Have ships larger than 1x1
​
## Data Model
​
I decided to use a Board class as my model. The game creates two instances of the Board class to hold the player's and the computer's board.
​
The Board class stores the board size, the number of ships, the position of the ships, the guesses against that board, and details such as the board type (player's board or computer) and the player's name.
​
The class also has methods to help play the game, such as a `print` method to print out the current board, an `add_ships` method to add ships to the board and an `add_guess` method to add a guess and return the result.

## Testing
​
I have manually tested this project by doing the following:
​
* Passed the code through a PEP8 linter and confirmed there are no problems
* Given invalid inputs: strings when numbers are expected, out of bounds inputs, same input twice
* Tested in my local terminal and the Code Institute Heroku terminal
​
### Bugs
​
#### Solved Bugs
​
* When I wrote the project, I was getting index errors because I had forgotten that the lists are zero indexed. I fixed this by adding `size - 1` where necessary
* My `validate_coordinates` function was returning false positives because I hadn't structured the `if` statement properly
​
### Remaining Bugs
​
* No bugs remaining that I'm aware of.
​
### Validator Testing
​
* PEP8
    * No errors were returned from PEP8online.com
	![pep8-screenshot](documents/testing/pep8.png]
​
## Deployment
​
This project was deployed using Code Institute's mock terminal for Heroku.
​
* Steps for deployment:
    * Fork or clone this repository
		- `git clone https://github.com/benjimansutton/warship.git`
    * Create a new [Heroku](https://www.heroku.com) app
    * Set the buildpacks to `Python` and `NodeJS` in that order
    * Link the Heroku app to the GitHub repository
    * Click on **Deploy**
	* Make sure to freeze the requirements.txt file
		- `pip3 freeze --local > requirements.txt`
​
### Local Deployment
​
In order to make a local copy of this project, you can clone it. In your IDE Terminal, type the following command to clone my repository:
​
- `git clone https://github.com/benjimansutton/warship.git`
​
You will also need to install the required packages from the [requirements.txt](requirements.txt), and you can do that using this command:
	- `pip3 install -r requirements.txt`
​
​

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.
​
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/benjimansutton/warship)
​
## Credits
​
* Code Institute for the [deployment terminal](https://github.com/Code-Institute-Org/python-essentials-template)
* Wikipedia for the details of Text-based games
Collapse


Thank You
Benjiman Sutton




