# User input 2


word = input("what is your word? :")
print( " Your word is " + str(word))
scores = {"a":1, "b":3, "c":3, "d":2, "e":1,"f":4, "g":2,"h":4, "i":1, "j":8,
           "k":5, "l":1, "m":3, "n":1, "o":1, "p":3, "q":10, "r":1, "s":1, "t":1, "w":4, "v":4, "y":4,
           "u":1, "x":8, "z":10}
def scrabble_score (word):
 total=0
 word= word.lower()
 for letter in word:
   total +=scores[letter]
 print ("your score is " + str(total))
scrabble_score(word)