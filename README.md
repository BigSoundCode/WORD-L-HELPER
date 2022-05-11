# WORD-L-HELPER
#### Video Demo:  https://www.youtube.com/watch?v=OIoCIBKGzOM
#### Description:

WORD-L-HELPER is a web application that helps in solving the New York Time's daily word puzzle.

At first, WORD-L-HELPER will offer up a random 5 letter word from the text file containing a large list of 5 letter words to help the user get started.

Following this the user will input letters into an input field indicating location and color (green, yellow or gray) of letters that Wordle has indicated are either in the correct location, somewhere within the word or not contained in the word.

Using some loop structures the application will systematically eliminate words that contain letters that don't line up with the colors provided by Wordle. It will then serve up suggestions based off user input until the puzzle is successfully solved.

There is no API or interface with the actual Wordle site, it is purely dependent on direct user input.

Front end is built with HTML/CSS & Javascript and the back end with Python. Jinja and FLASK are used as well.

Code:

styles.css is the stylesheet used to customize the Bootstrap CSS that was used heavily for the project.

home.html is the structure of the page. It includes the inputs, buttons and jinja syntax to return suggestions to the user. There is a little bit of javascript used to provide a better user experience on the input fields.

5letterwords.txt is the text file containing a list of over 5000 5 letter words on Stanford's website: https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt

It was debated whether or not to use a database for this project to store the words. Ultimately it was decided a text file would suffice as there was no relational aspect to the data. Although SQL is powerful, I decided that it would make the code unnecessarily complex.

app.py contains all of the logic for the program, it uses POST requests to obtain input data and then filter out the words not matching the WORDLE feedback. It relies on the flask framework to make the web app run. Originally, I thought I would make use of regular expressions to filter the words. This became increasingly complicated to implement as I imagined the different possible combinations of REs to check for, and decided for loops were much more practical for this application.

The biggest challenge was finding how to store the list of gray letters after each post request. I considered several approaches before re-discovering the session object as an appropriate tool for the job. I considered a database however as the data only needs to be stored temporarily that this was inappropriate. Further, this would not scale as the the database would need to store inputs for each user visiting the site. I tried keeping the data in an array and javascript to store the data client side and then send it back and forth with AJAX/JQUERY requests but this solution seemed convoluted. Ultimately, storing the list of gray letters in the session object seemed to be the right answer.

temp.py is a simple python script to take the list of 5 letter words, strip and whitespace characters and then output a file containing the words in all uppercase. The app.py program converts all the user input to uppercase to ensure the program is case insensitive. I have included this incase people want to contribute to my program and improve the list of words.
