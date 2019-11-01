#1 Read in a .txt file and parse the content.
#2 Perform a frequency analysis of the characters and words in the text file.
#3 Output the frequency of the most occurring words in the text file to a CSV file.
#4 Present your frequency analysis of the characters visually using the Matplotlib plotting library.
#5 Produce a Markdown file in your repository directory that combines your findings in one place.
import csv
import matplotlib.pyplot as plt

# OBJECTIVE 1 - Reading a text file and parsing the contents to a STRING and an ARRAY
f = open("textfile1","r")   # Opens the specified textfile and reads from it
theString = f.read()        # Assigns everything from the textfile to a str-variable

# OBJECTIVE 2 - Frequency analysis the characters within the text file using .count()
# <string name>.count(substring, start=..., end=...) This returns the number of substrings within the string
A = theString.count("A"); a = theString.count("a"); B = theString.count("B"); b = theString.count("b")
C = theString.count("C"); c = theString.count("c"); D = theString.count("D"); d = theString.count("d")
E = theString.count("E"); e = theString.count("e"); F = theString.count("F"); f = theString.count("f")
G = theString.count("G"); g = theString.count("g"); H = theString.count("H"); h = theString.count("h")
I = theString.count("I"); i = theString.count("i"); J = theString.count("J"); j = theString.count("j")
K = theString.count("K"); k = theString.count("k"); L = theString.count("L"); l = theString.count("l")
M = theString.count("M"); m = theString.count("m"); N = theString.count("N"); n = theString.count("n")
O = theString.count("O"); o = theString.count("o"); P = theString.count("P"); p = theString.count("p")
Q = theString.count("Q"); q = theString.count("q"); R = theString.count("R"); r = theString.count("r")
S = theString.count("S"); s = theString.count("s"); T = theString.count("T"); t = theString.count("t")
U = theString.count("U"); u = theString.count("u"); V = theString.count("V"); v = theString.count("v")
W = theString.count("W"); w = theString.count("w"); X = theString.count("X"); x = theString.count("x")
Y = theString.count("Y"); y = theString.count("y"); Z = theString.count("Z"); z = theString.count("z")
fullstop = theString.count("."); comma = theString.count(","); hyphen = theString.count("-")
space = theString.count(" "); newline = theString.count("\n"); ePoint = theString.count("!"); Qmark = theString.count("?")
apostrophe = theString.count("'"); elipses = theString.count("..."); colon = theString.count(":")
semiColon = theString.count(";")

alphabet = [A,a,B,b,C,c,D,d,E,e,F,f,G,g,H,h,I,i,J,j,K,k,L,l,M,m,N,n,O,o,P,p,Q,q,R,r,S,s,T,t,U,u,V,v,W,w,X,x,Y,y,Z,z,]
punctuation = [space,newline,fullstop,comma,hyphen,ePoint,Qmark,apostrophe,elipses,colon,semiColon]

# Remove UPPERCASE letters and PUNCTUATION for accurate count
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
print(alphabet)

# OBJECTIVE 3 - Writing top 10 most used words to a CSV file
# Following functions are used from library csv found @ and credit to https://docs.python.org/3/library/csv.html
max = len(theInfoArray)-1
with open("test.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=" ",
                            quotechar="|", quoting=csv.QUOTE_MINIMAL)
    # Uses "max" to refer to the top value, max-1, max-2, ... used to refer to the next values
    writer.writerow([theInfoArray[max][0]] + [theInfoArray[max][1]])
    writer.writerow([theInfoArray[max-1][0]] + [theInfoArray[max-1][1]])
    writer.writerow([theInfoArray[max-2][0]] + [theInfoArray[max-2][1]])
    writer.writerow([theInfoArray[max-3][0]] + [theInfoArray[max-3][1]])
    writer.writerow([theInfoArray[max-4][0]] + [theInfoArray[max-4][1]])
    writer.writerow([theInfoArray[max-5][0]] + [theInfoArray[max-5][1]])
    writer.writerow([theInfoArray[max-6][0]] + [theInfoArray[max-6][1]])
    writer.writerow([theInfoArray[max-7][0]] + [theInfoArray[max-7][1]])
    writer.writerow([theInfoArray[max-8][0]] + [theInfoArray[max-8][1]])
    writer.writerow([theInfoArray[max-9][0]] + [theInfoArray[max-9][1]])

# OBJECTIVE 4 - Visually representing character frequency analysis via MATPLOTLIB
# Following functions are used from matplotlib @ https://matplotlib.org/tutorials/introductory/pyplot.html

# Plotting ALPHABET Characters
alphabetNames = ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l"
        ,"M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z"]
alphabetValues = alphabet
plt.figure(figsize=(19.20, 10.80))
plt.bar(alphabetNames, alphabetValues)

# Plotting PUNCTUATION Characters
punctuationNames = ["space","newline","fullstop","comma","hyphen","ePoint","Qmark","apostrophe","elipses","colon",
                    "semi-colon"]
punctuationValues = punctuation
plt.figure(figsize=(19.20,10.80))
plt.bar(punctuationNames,punctuationValues)

plt.show()




