# manipulating strings


s = "Oh wherefore art thou, my dearest silly boy Romeo"
print(s)
print(len(s))

print("Check for the letter 'e':")
print("e" in s)

print("Count how manny 'e's exist:")
e = 0
for i in s:
    if i == 'e':
        e += 1
print(e)

print('Remove all of the spaces!')
newstring = ''
for i in s:
    #print(i)
    if i != ' ':
        newstring = newstring + i
print(newstring)

# set all to lowercase
print(s.lower())

#set all to uppercase
print(s.upper())


