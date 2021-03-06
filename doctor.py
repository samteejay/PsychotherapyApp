"""
Program: doctor.py
Author: Samuel Tijani
Conducts an interactive session of nondirective psychotherapy.
"""

import random

hedges = ("Please tell me more.",
          "Many of my patients tell me the same thing.",
          "Please continue.")

qualifiers = ("Why do you say that ",
              "You seem to think that ",
              "Can you explain why ")

replacements = {"I":"you", "me":"you", "my":"your",
                "we":"you", "us":"you", "mine":"yours"} 

def reply(sentence):
    """Builds and returns a reply to the sentence."""
    probability = random.randint(1, 4)
    if probability == 1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + change_person(sentence)
		
def change_person(sentence):
    """Replaces first person pronouns with second person
    pronouns."""
    
    reply_words = map(lambda word: replacements.get(word, word), sentence.split())
    return " ".join(reply_words)

def main():
    """Handles the interaction between patient and doctor."""
    print("Good morning, I hope you are well today.")
    print("What can I do for you?")
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print("Have a nice day!")
            break
        print(reply(sentence))


main()
