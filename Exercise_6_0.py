# manipulating strings

# play with whatever I enter

entry = input("This will print forwards: ")

for i in entry:
    print(i)

entry = input("This will print backwards: ")

# for i in entry:
#     print(len(entry)-i)
# Doesn't work for now, try a different way

i = 0
while i < len(entry):
    print(entry[len(entry)-i-1])
    i += 1
# ok this one works, yay!
