txt1 = 'Hello World'
txt2 = 'o'
print(txt1.rfind(txt2))   # returns the last index of the str instance if present otherwise -1 if no such index exists
print(txt1.rfind(txt2, 10, 0))  # rfind() is restricted to search for a str from beginning to end
if txt1.rfind(txt2, 0, len(txt1)) > -1:
    print('Has repeated char {}.'.format(txt2))

