#!C:\Users\ADITYA\AppData\Local\Programs\Python\Python36-32\python.exe  

print("Content-Type: text/html")
print()

import cgi
import random
form = cgi.FieldStorage()
reds = 0
whites = 0

if "answer" in form:
    answer = form.getvalue("answer")
else:
    answer = ""
    for i in range(4):
        answer += str(random.randint(0, 9))

if "guess" in form:
    guess = form.getvalue("guess")
    for key, digit in enumerate(guess):
        if digit == answer[key]:
            reds += 1
        else:
            for answerDigit in answer:
                if answerDigit == digit:
                    whites += 1
                    break
else:
    guess = ""

if "numberOfGuesses" in form:
    numberOfGuesses = int(form.getvalue("numberOfGuesses")) + 1
else:
    numberOfGuesses = 0

if numberOfGuesses == 0:
    message = "I've chosen a 4 digit number. Can you guess it?"
elif reds == 4:
    message = "Well done! You got in " + str(numberOfGuesses) + " guesses. <a href=''>Play again</a>"
else:
    message = "You have " + str(reds) + " correct digit(s) in the right place, and " + str(whites) + " correct digit(s) in the wrong place. You have had " + str(numberOfGuesses) + " guess(es)."



print("""
<h1>Mastermind</h1>
<p>I've chosen a 4 digit number. Can you guess it?</p>
<form method="post">""")
print("""
<input type="text" name="guess" value="'+guess+'">""")
print("""
<input type="hidden" name="answer" value = "'+answer+'">
<input type="hidden" name="numberOfGuesses" value = "0">
<input type="submit" value="Guess!">
</form>
""")