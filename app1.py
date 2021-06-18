import json
import difflib
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    
    if word in data:
        return " ".join(data[word])
    elif get_close_matches(word, data, cutoff=0.8):
        new_word = get_close_matches(word, data, cutoff=0.8)[0]

        input_word = input("Did you mean %s instead? Type 'Y' if yes and 'N' if no " % new_word)
        if input_word.lower() == "y":
            return data[new_word] # " ".join(data[new_word])
        elif input_word.lower() == "n":
            return "no such word found."
        else:
            return "We did not understand you! "
    else:
        return f"{word} was not found."


word = input("Enter word: ")

result = translate(word)
if isinstance(result, list):
    for stroutput in result:
        print(stroutput)
else:
    print(result)