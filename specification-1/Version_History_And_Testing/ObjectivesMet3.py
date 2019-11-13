#1 Read in a .txt file and parse the content.
#2 Perform a frequency analysis of the characters and words in the text file.
#3 Output the frequency of the most occurring words in the text file to a CSV file.
#4 Present your frequency analysis of the characters visually using the Matplotlib plotting library.
#5 Produce a Markdown file in your repository directory that combines your findings in one place.
import csv

f = open("textfile1","r")   # Opens the specified textfile and reads from it
theString = f.read()        # Assigns everything from the textfile to a str-variable
theArray = theString.split()# Assigns each word to an element in an array/list

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
space = theString.count(""); newline = theString.count("\n"); ePoint = theString.count("!"); Qmark = theString.count("?")
apostrophe = theString.count("'")

alphabet = [A,a,B,b,C,c,D,d,E,e,F,f,G,g,H,h,I,i,J,j,K,k,L,l,M,m,N,n,O,o,P,p,Q,q,R,r,S,s,T,t,U,u,V,v,W,w,X,x,Y,y,Z,z,
            space,newline,fullstop,comma,hyphen,ePoint,Qmark,apostrophe]
theInfoArray = [] # A 2D array storing a WORD and NUMBER of appearances [WORD][No.]
# Calculates number of each words without storing words
for i in range(0,len(theArray)):
    # When a queried word is found, it is deleted to prevent recounts.
    tempCount = 0
    tempWord = theArray[i]
    if theArray[i] != "" and theArray[i] != "." and theArray[i] != "-" and theArray[i] != "?" and theArray[i] != "!"\
            and theArray[i] != "\n" and theArray[i] != "," and theArray[i] != "'":
        for i2 in range(0,len(theArray)):
            if theArray[i2] == tempWord:
                theArray[i2] = ""
                tempCount += 1
        print(tempCount,tempWord)
        theInfoArray.append([tempWord,tempCount])
    # theInfoArray now contains a WORD and NUMBER-OF-APPEARANCES: theInfoArray[data-point][0=Word|1=Appearances]
    # Now do a bubble sort moving the most the occurring words to the right most side!!!

print(theInfoArray)

# Bubble sort on a 2D array ASCENDING ORDER
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

# Gonna use "import csv" located @ https://docs.python.org/3/library/csv.html
# So that I can write to a CSV file

max = len(theInfoArray)-1
# Below code is NOT written by and is taken from CSV library, credit to https://docs.python.org/3/library/csv.html
with open("test.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=" ",
                            quotechar="|", quoting=csv.QUOTE_MINIMAL)
    # Writes the top
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

