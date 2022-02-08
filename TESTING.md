# Warship Testing
​
Warship has been tested both in the terminal in Gitpod and the Code Institute Heroku terminal

Whilst testing the playability of the game an error that was come upon was the terminal would fill very quickly

To over come the terminal filling with commands the 'clear' function was added to the game
​
[Here is the live version of my project.](https://warship-app.herokuapp.com/)
​
![Screenshots](documents/testing/warship_game_play.png)
​
## Issues

* Layout of the game - fixed with following the pep8 guidelines for the length of the command
* Indentation - during the build of the game, indentation errors caused problems with the game running.
​
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
* When I wrote the project, I was getting errors that where linked to functions not calling due to indentation errors
* My 'replay_game' function was not calling due to an error with the 'if' statement as i was calling an 'else' instead of an 'elif' statement first
​
### Remaining Bugs
​
* No bugs remaining that I'm aware of.
​
### Validator Testing
​
* PEP8
    * Errors were returned from PEP8online.com
	![PEP8 Errors Screen Shot 1](documents/testing/pep8_errors_1.png]
    * Multiple errors were returned from PEP8online.com
    ![PEP8 Errors Screen Shot 2](documents/testing/pep8_errors_2.png]
    * No errors were returned from PEP8online.com
    ![PEP8 No Errors](documents/testing/pep8_no_errors.png]