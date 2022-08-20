# Dictionaries


file = open('exit survey.txt')

text = file.read() # crush the lines down into raw text
text = text.lower() # covert all upper case characters to lower case
#print(text)

#print(text.split())

wordcount = dict() #declare an empty dictionary to store the word count in
for word in text.split():
    # if word in wordcount:
    #     wordcount[word] += 1
    # else:
    #     wordcount[word] = 1
    wordcount[word] = wordcount.get(word,0) + 1 #use this function to substitute for the above

print(max(wordcount.values()))
bigcount = None
bigword = None
for word,count in wordcount.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)