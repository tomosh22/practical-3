''' FIRST ATTEMPT - FAILED -
print(theArray)
for word in range(0,len(theArray)):
    for char in range(0,len(theArray[word])):
        if theArray[word][char] == ".":
            (theArray[word][char]) = "" # Strings are immutable hence characters cannot be edited
            # Therefore assign each character to a new array in which all punctuation is ignored only record characters
print(theArray)
'''


'''
print('a bar is a bar, essentially'.replace('bar', 'pub'))
# 'a pub is a pub, essentially'
'''

'''
theNewArray = theArray
print(theNewArray)
for i in range(0,len(theArray)):
    theNewArray[i] = ""

for word in range(0,len(theArray)):
    for char in range(0,len(theArray[word])):
        if theArray[word][char] != ".":
            theNewArray[word][char] == theArray[word][char]

print(theNewArray)
print(theArray)
'''
'''
print("Before modification: ",theArray)
for word in range(0,len(theArray)):
    for char in range(0,len(theArray[word])):
        if theArray[word][char] == ".":
            theArray[word][char].replace("."," ")
print("After modification: ",theArray)
'''
# Success! Found a method to remove punctuation. Implement this before the words are counted in the main file.
import csv
import matplotlib.pyplot as plt
'''
# OBJECTIVE 1 - Reading a text file and parsing the contents to a STRING and an ARRAY
f = open("textfile2","r")   # Opens the specified textfile and reads from it
theString = f.read()        # Assigns everything from the textfile to a str-variable
# Remove UPPERCASE letters and PUNCTUATION for accurate count
theString.replace(",","")
theArray = theString.split()# Assigns each word to an element in an array/list

theNewString = theString
theNewString = theNewString.replace(".","")
theNewString = theNewString.replace("?","")
theNewString = theNewString.replace("!","")
theNewString = theNewString.replace("...","")
theNewString = theNewString.replace(":","")
theNewString = theNewString.replace(";","")
theNewString = theNewString.replace(",","")

print(theString)
print(theNewString)
'''
f = open("textfile1","r")
theString = f.read()
removePunc = [".", "?", "!", "...", ":", ";", ",","(",")","[","]"]
for iremove in range(0,len(removePunc)):
    theString = theString.replace(removePunc[iremove],"")
removeUpperCase = ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l"
        ,"M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z"]
# 0 = UpperA, 1 = LowerA, 2 = UpperB, 3 = LowerB THEREFORE (Even = Upper) AND (Odd = Lower)
for iremove in range(0,len(removeUpperCase),2):
    theString = theString.replace(removeUpperCase[iremove],removeUpperCase[iremove+1])
theArray = theString.split()

theInfoArray = [] # A 2D array storing a WORD and NUMBER of appearances [WORD][No.]
# Calculates number of each words without storing words
for i in range(0,len(theArray)):
    # When a queried word is found, it is deleted to prevent recounts.
    tempCount = 0
    tempWord = theArray[i]
    if theArray[i] != "" and theArray[i] != "." and theArray[i] != "-" and theArray[i] != "?" and theArray[i] != "!"\
            and theArray[i] != "\n" and theArray[i] != "," and theArray[i] != "'" and theArray[i] != "..."\
        and theArray[i] != ":" and theArray[i] != ";":
        for i2 in range(0,len(theArray)):
            if theArray[i2] == tempWord:
                theArray[i2] = ""
                tempCount += 1
        #print(tempCount,tempWord)
        theInfoArray.append([tempWord,tempCount])
    # theInfoArray now contains a WORD and NUMBER-OF-APPEARANCES: theInfoArray[data-point][0=Word|1=Appearances]
    # Now do a bubble sort moving the most the occurring words to the right most side!!!

# OBJECTIVE 3 - Writing top 10 most used words to a CSV file
# Bubble sort on a 2D array ASCENDING ORDER
# This is done so that the top ten most used words can be referenced using {len, len-1, len-2,...}
temp = [["",0]]
loop = True
swapped = False
while loop == True:
    for i in range(0,len(theInfoArray)-1): # Cannot compare last item to next item(OUT OF RANGE)therefore stop 2nd to last item
        if theInfoArray[i][1] > theInfoArray[i+1][1]:
            temp[0][0] = theInfoArray[i][0]
            temp[0][1] = theInfoArray[i][1]
            theInfoArray[i][0] = theInfoArray[i+1][0]
            theInfoArray[i][1] = theInfoArray[i+1][1]
            theInfoArray[i+1][0] = temp[0][0]
            theInfoArray[i+1][1] = temp[0][1]
            swapped = True
    if swapped == True:
        loop = True
        swapped = False
    else:
        loop = False

print(theInfoArray)
