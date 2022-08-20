#manipulating lists

a = [1,2,3]
b = [4,5,6]
c = a + b

print(c)

print(c[:4])

print(c.count(4)) # count how many 1's exist in the list

c.reverse()
print(c)

c.append('grapes')
print(c)
