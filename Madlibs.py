#This is the first of 12 beginner projects presented by Kylie Ying. It shows concatenations.

#first ask participant to input some words

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

#then adds those words to a paragraph

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)