'''
Dictionary Project with the use of json (java script object notation) file
'''

import json
from difflib import get_close_matches

def repeat():
    rep=input("Would you like to search another word? Y/N:")
    if rep.strip().upper()=="Y":
        inpword()
    elif rep.strip().upper()=="N":
        print("Thank you for using our application...")
        exit()
    else:
        print("Wrong input...")
        repeat()

def inpword():
    word= input("Enter a word:")
    print(*meaning(word), sep="\n")
    print()
    repeat()

def meaning(word):
    word= word.lower().strip()
    if word in data:
        return data[word]
    elif word not in data:
        print(word, " not found...\n Did you mean that?")
        print(get_close_matches(word, data.keys()))
        print()
        repeat()
    else:
        print("Word not found...")
        repeat()

data= json.load(open("data1.json"))
print(type(data))

inpword()
#for i in data:
    #print(i)