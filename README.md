# Bombing Blasting Battleships
![responsive-image](documentation/01-responsive-design.png)

## Features
### Existing Features

![welcome-section-image](documentation/02-welcome-statement.png)

![initial-inputs-image](documentation/03-initial-inputs.png)

![initial-boards-image](documentation/04-initial-boards.png)

![round-start-image](documentation/05-guess-inputs.png)

![board-return-01-image](documentation/06-board-results-01.png)

![board-return-02-image](documentation/07-board-results-02.png)

![invalid-attempts-image](documentation/08-invalid-attempts.png)

![board-result-01-image](documentation/09-board-result-01.png)

![board-result-02-image](documentation/10-board-result-02.png)

![end-of-game-image](documentation/11-end-game.png)

### Features Left to Implement

## Languages and Resources

* [Python](https://www.python.org/) - The language used to write the terminal-based game.
* [Code Institute Template P3](https://github.com/Code-Institute-Org/p3-template) - The template used to build the site.
* [HTML5](https://html.spec.whatwg.org/multipage/) - The language provided by the Code Institute template. 
* [JavaScript](https://www.w3.org/TR/css-2022/)  - The language provided by the Code Institute template.  
* [GitHub](https://github.com/) - Repository for the site’s code.
* [Codeanywhere](https://www.codecademy.com/)  - The IDE used to write the code.
* [Am I Responsive](https://ui.dev/amiresponsive) - As site used to test the responsiveness of the page.
* [Heroku](https://www.heroku.com/home) - To deploy the site.

## Testing

The page has been fully tested in two major ways manually and using the build-in checks and Python validator.

### Manual Testing

* The features on the page include the run program button and the terminal-based game itself, both are very responsive and interactive which work perfectly.
* With the terminal-based game the following has been checked:
    - Valid inputs: All input features in the game have been fully tested. Starting with name input when a name is entered all future printed iterations are correct and capitalize the name throughout the game, this was tested by entering a lowercase name.
    - Secondly, the grid input has been fully tested, it has been checked that any number equalling three or lower does not accept and encourages the user to enter a valid number, and all non-integer strings are not accepted either this was tested by placing incorrect values into this input. It was also tested that the integer inputted does print the desired number of spaces on the board.
    - In the same way the guess row and guess col inputs have been tested, each does not accept any non-integer values and requires the user to enter a number between zero and the desired number of spaces minus one. Any other values outside this range receive an invalid attempt and once this happens three times the game ends. All these features have been tested by inserting incorrect data into the inputs.
    - The feature of submitting the same values into the guess inputs has also been tested and it does return the statement  that the user has already guessed that position. Additionally to this, it has been tested that the imputed coordinates do correlate to those on the boards.
    - Overall all the inputted sections of code have been fully tested and all respond to the kind of data a user might insert.
    - The game has been played numerous times and always delivers the correct score and result of who won correctly too.

* The game has also undergone input from the built-in suggestion of what the IDE ‘Codeanywhere’ suggests, particularly to the display and the organization of the code. 

### Validator Testing
![validator-image](documentation/12-validator-check.png)

* The Bombing Blasting Battleships page has no errors and when passing through the official [CI Python Linter (validator)](https://pep8ci.herokuapp.com/) the result returns ‘All clear, no errors found’.

### Bugs

#### Fixed Bugs

In the context of bugs there were a few minor simple fixes, however, there were two major bugs in the development of the code:

* First was in the context of when the computer would choose its grid values. The values the computer makes come from a random number function which generates random numbers between zero and the desired grid size. The computer uses this function for its entries, however, upon first testing, the game would often crash after the user entered their values, however, it wasn’t consistent because offer or not the player could go as far as the sixth round and other times it would be hard to get to round two without the game crashing. Therefore, with an investigation, it was discovered that, since the indexing of the grid begins at zero in Python it considers zero as the first value. Thus the random number function was producing numbers between zero and the inputted desired grid size, which by doing so made the computer enter grid points that were out of range. To fix this the function was adjusted so the range would be between zero and the desired number minus one. 

* The Second major bug was the fact that in the early stages of the site, the player would be able to see where the ships were placed on the computer's board. This completely took away the whole point of the game since the user would be able to win within four rounds and cheat because the ships were on display. Therefore to fix this problem the solution was to have three boards, one for the player and two for the computer. The first computer board would be the underground board where the user's actions would impact it, and the other would be a display board. A board that would only display the hit points and points which the player has interacted with. Thus this was created by creating a third variable labeled hidden and making sure that the actual computer board was being updated and updating the display board with the correct values.

#### Unfixed Bugs

* At this current point there are NO bugs that were left unfixed. 

## Deployment

The site was deployed to Heroku. The steps to deploy are as follows:
* On the Heroku dashboard click ‘New’, and continue to ‘Create new app’
* Create a name for your deployed project and select the region of the world you reside in.
* From here navigate to the settings tab of the project, continue to the ‘Config Vars’ section, and click ‘Reveal Config Vars.
* Within the ‘KEY’ input insert ‘PORT' and within the ‘VALUE’ input insert ‘8000’ and continue to click ‘Add’.
* After this continue to the Buildpacks section and click ‘Add buildpack’. 
* Here select ‘python’ and click ‘Add Buildpack’ again. Repeat this step but instead of ‘python’ click on ‘nodejs’. Once completed check that buildpack ‘python’ is ABOVE that of ‘nodejs’.
* From here return to the deploy tab of the project, and go to Deployment method, here select GitHub (or the service your repo is saved to).
* Once connected within the input labeled ‘repo-name’ insert the correct name of the repo saved on your GitHub account.
* Then from here click ‘Connect’.
* Finally in the Manual deploy section click the ‘Deploy Branch’ button from here the code will take some time to deploy once this is done, click on the button labeled ‘View’ to see your LIVE project deployed. 

You can view my live site of Bombing Blasting Battleships [here.](https://bombing-blasting-battleships-f95b679c02b6.herokuapp.com/)

## Credits

### Content
* The code template for the site was provided by [Code Institute](https://github.com/Code-Institute-Org/p3-template)
* The idea of the game comes from the common game of [Battleships](https://en.wikipedia.org/wiki/Battleship_(game))
* Inspiration for the basic look and functionality was influenced by [ULTIMATE BATTLESHIPS](https://p3-battleships.herokuapp.com/)
* The project [Love Sandwiches](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode) was a huge help in understanding the use of functions and importation into the Python file. As well as the basic structure of code.
* The YouTube channel [Programming with Mosh](https://www.youtube.com/@programmingwithmosh/featured) and a few videos helped the process of overcoming more complex areas of the site such as placing the ships function.
* The Youtube video [Python Tutorial: Generate Random Numbers and Data Using the Random Module](https://www.youtube.com/watch?v=KzqSDvzOFNA&t=531s) by Corey Schafer was huge help in concern to import and generate random numbers by importing random.

### Media
* No media files were used in the creation of this site.


