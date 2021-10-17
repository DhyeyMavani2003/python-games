#flashcards.py

#import json module from python3
import json

#open file and parse the json
with open('me-capitals.json', 'r') as f:
    data = json.load(f)

# initialize total as the length of the cards array
total = len(data["cards"])
# initialize score as 0
score = 0

for i in data["cards"]:
    guess = input(i["q"] + " > ")

    if guess.lower() == i["a"].lower():
        # increment score up one
        score += 1
        # interpolate score and total into the response
        print(f"Correct! Current score: {score}/{total}")
    else:
        print("Incorrect! The correct answer was", i["a"])
        print(f"Current score: {score}/{total}")
