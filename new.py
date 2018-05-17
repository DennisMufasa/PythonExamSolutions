def is_isogram(word):

    if type(word) != str:

        raise TypeError('Argument should be a string')

    elif word == "":
        return (word, False)
    else:
        word = word.lower()
        for char in word:
            if word.count(char) > 1:
                return (word, False)
            else:
                return (word, True)



def is_isogram(word):
    return (word,True) if word and len(set(word)) == len(word) else (word,False)


