# # String
# break  the string into list of words
str = 'hi dee hi how are you mr dee'
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts :
            counts[word] +=1
        else:
            counts[word] = 1

    return counts

print(word_count('hi dee hi how are you mr dee'))
