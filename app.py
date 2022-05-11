import os


from flask_session import Session
from flask import Flask, flash, redirect, render_template, request, session
from tempfile import mkdtemp
import random


#Configure application
app = Flask(__name__)

app.secret_key = '\xba\xfa\xecP\x1c\x06u\x86\xa6\xf5\xc8\xd6S\xa8\xebJ\xdd\x0b\x17\x00\xb3a*\xea\xf0\xb7\xc0\xbc\x00\x10\x93\xed'

#Auto reload templates
app.config["TEMPLATES_AUTO_RELOAD"] = True



app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)




@app.route("/", methods=["GET","POST"])
def home():
    if 'gray_list' in session:
        copy = session['gray_list']
    else:
        session['gray_list'] = []


    if request.method == "POST":
        #open up list of words and store in list.

        fhand = open("newwords.txt")
        words = fhand.read().split()
        newwords = []
        #Provide user with initial random word from list of 5 letter words.
        if not request.form.get("one") and not request.form.get("W"):
            x = random.randrange(5757)
            word = words[x]
            return render_template("home.html", x=x, word=word)
        #Set lists to use to iterate through user inputs and store in lists.

        boxes = ["one", "two", "three", "four", "five"]
        letters = ["W", "O", "R", "D", "L"]
        green = [None, None, None, None, None]
        yellow = [None, None, None, None, None]
        gray = [None, None, None, None, None]
        #Get users green, yellow and gray letters from HTML form.
        for i in range(5):
            if request.form.get(boxes[i]) == "green":
                green[i] = request.form.get(letters[i])
                green[i] = green[i].upper()

            elif request.form.get(boxes[i]) == "yellow":
                yellow[i] = request.form.get(letters[i])
                yellow[i] = yellow[i].upper()

            elif request.form.get(boxes[i]) == "gray":
                gray[i] = request.form.get(letters[i])
                gray[i] = gray[i].upper()
                copy.append(gray[i])

        session['gray_list'] = copy

        for i in range(5):
            #eliminate words that don't match positions of green letters.
            for index, word in enumerate(words):
                if green[i] != None:
                    if word[i] != green[i]:
                        words[index] = '00000'
                #delete words not containing yellow letters, or words where letter matches position of yellow letter
                if yellow[i] != None:
                    if yellow[i] not in word or word[i] == yellow[i]:
                        words[index] = '00000'
                #delete words containing gray letters
                if gray[i] != None:
                    if word[i] == gray[i]:
                        words[index] = '00000'
                    if word[i] in gray and word[i] not in green:
                        words[index] = '00000'
                    if word[i] in session['gray_list']:
                        words[index] = '00000'

        for word in words:
            if word != '00000':
                newwords.append(word)



        return render_template("home.html", newwords=newwords)





    elif request.method == "GET":
        return render_template("home.html")