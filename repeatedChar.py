from collections import Counter


def repeated_char(word):
    # creating a dictionary using the method counter that has strings as keys and their frequencies as values
    data = Counter(word)
    j = -1

    for i in data.values():
        j = j + 1
        if i > 1:
            print(data.keys()[j])


if __name__ =="__main__":
    word = 'hello'
    repeated_char(word)


