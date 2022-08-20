# use of the split function on strings!

try:
    file = open('main.py')
except:
    quit()

text = file.read()
words = text.split()
print(words)