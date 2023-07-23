from flask import Flask, redirect, url_for, render_template, request
from pymongo import MongoClient
import random
from timeit import default_timer as timer

client = MongoClient('localhost', 27017)
db = client.FSP

collection6 = db.wordList6
collection7 = db.wordList7
collection8 = db.wordList8

class Counter:
    count6 = 0
    count7 = 0
    count8 = 0
    time6 = 0
    time7 = 0
    time8 = 0
    highscore6 = 0
    highscore7 = 0
    highscore8 = 0
    besttime6 = "-"
    besttime7 = "-"
    besttime8 = "-"
    avgtime6 = 0
    avgtime7 = 0
    avgtime8 = 0
    
app = Flask(__name__)

# HOME PAGE
@app.route("/")
@app.route("/home", methods=["POST", "GET"])
def home():
    return render_template("home.html", 
                           highscore6 = Counter.highscore6, 
                           highscore7 = Counter.highscore7, 
                           highscore8 = Counter.highscore8, 
                           besttime6 = Counter.besttime6, 
                           besttime7 = Counter.besttime7, 
                           besttime8 = Counter.besttime8)

# SIX LETTER WORD CHALLENGE
@app.route("/sixLWC", methods=["POST", "GET"])
def sixLW():
    if request.method == "GET":
        cursor = collection6.find()
        no_of_records = collection6.count_documents({})
        global word 
        
        index = 0
        n = random.randint(0, no_of_records - 1)
        scrambled_word = ""
        
        for record in cursor: 
            if index == n:
                word = record["word"]
                break        
            index += 1

        scrambled_word = ''.join(random.sample(word, len(word)))
        while scrambled_word == word:
            scrambled_word = ''.join(random.sample(word, len(word)))
            
        global start
        start = timer()
        return render_template("sixLWC.html", scrambled_word = scrambled_word, count6 = Counter.count6, besttime6 = Counter.besttime6, avgtime6 = Counter.avgtime6)
    else:
        global end
        end = timer()
        guessed_word = request.form["guessed_word"]
        
        if guessed_word == word:
            Counter.time6 = round(end - start, 2)
            if Counter.avgtime6 == "-":
                Counter.avgtime6 = round(Counter.time6, 2)
            else:
                Counter.avgtime6 = round((Counter.avgtime6*Counter.count6 + Counter.time6) / (Counter.count6 + 1), 2)
            if Counter.besttime6 == "-" or Counter.besttime6 > Counter.time6:
                Counter.besttime6 = Counter.time6
            Counter.count6 += 1
            if Counter.count6 > Counter.highscore6:
                Counter.highscore6 = Counter.count6
        else:       
            Counter.count6 = 0
            
        return redirect(url_for("sixLW"))
    
# SEVEN LETTER WORD CHALLENGE
@app.route("/sevenLWC", methods=["POST", "GET"])
def sevenLW():
    if request.method == "GET":
        cursor = collection7.find()
        no_of_records = collection7.count_documents({})
        global word
        
        index = 0
        n = random.randint(0, no_of_records - 1)
        scrambled_word = ""
        
        for record in cursor: 
            if index == n:
                word = record["word"]
                break        
            index += 1
        
        scrambled_word = ''.join(random.sample(word, len(word)))
        while scrambled_word == word:
            scrambled_word = ''.join(random.sample(word, len(word)))
            
        global start
        start = timer()
        return render_template("sevenLWC.html", scrambled_word = scrambled_word, count7 = Counter.count7, besttime7 = Counter.besttime7, avgtime7 = Counter.avgtime7)
    else:
        global end
        end = timer()
        guessed_word = request.form["guessed_word"]
        
        if guessed_word == word:
            Counter.time7 = round(end - start, 2)
            if Counter.avgtime7 == "-":
                Counter.avgtime7 = round(Counter.time6, 2)
            else:
                Counter.avgtime7 = round((Counter.avgtime7*Counter.count7 + Counter.time7) / (Counter.count7 + 1), 2)
            if Counter.besttime7 == "-" or Counter.besttime7 > Counter.time7:
                Counter.besttime7 = Counter.time7
            Counter.count7 += 1
            if Counter.count7 > Counter.highscore7:
                Counter.highscore7 = Counter.count7
        else:   
            Counter.count7 = 0
            
        return redirect(url_for("sevenLW"))
    
# EIGHT LETTER WORD CHALLENGE
@app.route("/eightLWC", methods=["POST", "GET"])
def eightLW():
    if request.method == "GET":
        cursor = collection8.find()
        no_of_records = collection8.count_documents({})
        global word 
        
        index = 0
        n = random.randint(0, no_of_records - 1)
        scrambled_word = ""
        
        for record in cursor: 
            if index == n:
                word = record["word"]
                break        
            index += 1
        
        scrambled_word = ''.join(random.sample(word, len(word)))
        while scrambled_word == word:
            scrambled_word = ''.join(random.sample(word, len(word)))
            
        global start
        start = timer()
        return render_template("eightLWC.html", scrambled_word = scrambled_word, count8 = Counter.count8, besttime8 = Counter.besttime8, avgtime8 = Counter.avgtime8)
    else:
        global end
        end = timer()
        guessed_word = request.form["guessed_word"]
        
        if guessed_word == word:
            Counter.time8 = round(end - start, 2)
            if Counter.avgtime8 == "-":
                Counter.avgtime8 = round(Counter.time6, 2)
            else:
                Counter.avgtime8 = round((Counter.avgtime8*Counter.count8 + Counter.time8) / (Counter.count8 + 1), 2)
            if Counter.besttime8 == "-" or Counter.besttime8 > Counter.time8:
                Counter.besttime8 = Counter.time8
            Counter.count8 += 1
            if Counter.count8 > Counter.highscore8:
                Counter.highscore8 = Counter.count8
        else:   
            Counter.count8 = 0
            
        return redirect(url_for("eightLW"))

if __name__ == "__main__":
    app.run(debug=True)
    