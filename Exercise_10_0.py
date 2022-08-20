#tuples and such
from typing import List, Tuple, Union, Any

file = open('book.txt')

text = file.read() # crush the lines down into raw text
text = text.lower() # covert all upper case characters to lower case

count = 0
wordcount = dict() #declare an empty dictionary to store the word count in
for word in text.split():
    wordcount[word] = wordcount.get(word,0) + 1 #use this function to substitute for the above
    count += 1

lst = list()
for k,v in wordcount.items():
    #print(k,v)
    lst.append((v, k)) #reverse the value-key order

#print(tmp)
lst = sorted(lst, reverse = True)
#print(lst)

print("Out of ", count, " words:")
for v,k in lst[:10]:
    print(k,v)

#print( sorted([(v,k) for k,v in wordcount.items()]))

