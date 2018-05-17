def repeated_char(s):
    for i in range(len(s)):
        if i != s.rfind(s[i]):          # checks whether the last index of the string is equal to the current string and
            return True                 # returns True if it find that the last index is not equal to the current index
    return False                        # thus implying that the character at that index is repeated and vice-verser.


test = repeated_char('car')
print(test)






