import json
from difflib import get_close_matches

with open("data.json") as json_data:
    data = json.load(json_data)

def define(word):
    word = word.lower()

    if word in data:
        return data[word]
    
    elif word.title() in data: # if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    
    elif word.upper() in data: # in case user enters words like USA or NATO
        return data[word.upper()]

    elif get_close_matches(word, data.keys()):
        closest_match = get_close_matches(word, data.keys())[0]
        yes_or_no = input("Did you mean {}? Enter Y if yes or N if no: ".format(closest_match))
        if yes_or_no == "Y":
            return data[closest_match]
        elif yes_or_no == "N":
            return "This Word does not exist. Please double check it."
        else:
            return "Sorry, We did not understand your entry"

    else:
        return "This Word does not exist. Please double check it."


word = input("Enter the word here: ")

output = define(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
