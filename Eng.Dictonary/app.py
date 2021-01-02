import json
from difflib import get_close_matches

data = json.load(open("data/data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys()))>0:
        yn = input("Do you mean %s instead? Press 'y' for Yes, n for No : " %get_close_matches(w,data.keys())[0])
        yn = yn.lower()
        if yn == 'y':
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == 'n':
            return "the Word doesn't exist please dowuble check."
        else:
            return "invalid Entry"
    else:
        return "Given Word is not in data set please choose something else"


word = input("enter Word : ")

output = translate(word)
i = 0
if type(output) == list:
    for item in output:
        i =i+1
        print ( "%s."%i, item)
else:
    print (output)

#print(translate(word))