import csv
import matplotlib.pyplot as plt

def run():
    # OBJECTIVE 1 - Reading a text file and parsing the contents to a STRING and an ARRAY
    print("1) Place a text file within the same directory as this python file")
    print("2) Specify the file by inputting the name with the file extension")
    filename = str(input("Enter filename: "))
    print("3) Specify the character set used within the text file you wish to use")
    print("|utf-8|ascii|utf-16|utf-32|")
    encoding = str(input("Enter character-set-encoding: "))
    try:
        f = open(filename,"r",encoding=encoding)   # Opens the specified text file and reads from it
    except FileNotFoundError:
        print("\nERROR: File not found, please try again.\n")
        run()
    except LookupError:
        print("\nERROR: Encoding not found, please try again.\n")
        run()
    theString = f.read()        # Assigns everything from the text file to a str-variable
    #=====================================================================================

    # OBJECTIVE 2 - Frequency analysis of the characters within the text file using .count()
    # <string name>.count(substring, start=..., end=...) This returns the number of substrings within the string
    # The quantity of each character specified in the quotes is stored within a variable named equal to the char specified
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
    ''' Two categorised arrays store the quantities for later manipulation throughout the program '''
    alphabet = [A,a,B,b,C,c,D,d,E,e,F,f,G,g,H,h,I,i,J,j,K,k,L,l,M,m,N,n,O,o,P,p,Q,q,R,r,S,s,T,t,U,u,V,v,W,w,X,x,Y,y,Z,z,]
    punctuation = [space,newline,fullstop,comma,hyphen,ePoint,Qmark,apostrophe,elipses,colon,semiColon]

    ''' This removes UPPERCASE letters and PUNCTUATION-MARKS from the string storing the contents of the file 
    This was done because "right" and "right." were being counted as different values outputting an inaccurate word count
    this is achieved by using .replace to change any elements in "removePunc" and in "theString" to "".
    To change uppercase letters to lower, an array containing all upper and lower case letters was established named
    "removeUpperCase". When referring to an element within the array all uppercase letters hold an even index, 
    whereas all lowercase letters hold an odd index. Therefore a for loop only looking for uppercase letters by incrementing
    by 2, is replaced by the proceeding element that the for loop originally refers to. 
    '''
    removePunc = [".", "?", "!", "...", ":", ";", ",","(",")","[","]","—","_","-","—“","“","”","‘","#"]
    for iremove in range(0,len(removePunc)):
        theString = theString.replace(removePunc[iremove],"")
    removeUpperCase = ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l"
            ,"M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z"]
    # 0 = UpperA, 1 = LowerA, 2 = UpperB, 3 = LowerB THEREFORE (Even-Index = Upper) AND (Odd-Index = Lower)
    for iremove in range(0,len(removeUpperCase),2):
        theString = theString.replace(removeUpperCase[iremove],removeUpperCase[iremove+1])
    theArray = theString.split()

    '''An array where each element is a word from the textfile such that the text file is essentially stored within in an 
    array is established and called "theArray". A second array which is 2D, then recieves each word and the quantity of that
    word. This is achieved by using a nested for loop and if statement, firstly the word is checked such that if it is not a
    word it is not added to the 2D array. Secondly the second for loop is used to count the number of times the first word 
    appears, for each time it is found, it is deleted within "theArray" to prevent recounts/duplicates. Lastly the 2D array 
    then recieves the word and quanitity using .append()'''
    theInfoArray = [] # A 2D array storing a WORD and NUMBER of appearances [Data-Point][0=Word|1=Quantity]
    # Calculates quantity of each word without using pre-written functions specifying every word in existence
    for i in range(0,len(theArray)):
        # When a queried word is found, it is deleted to prevent recounts.
        tempCount = 0
        tempWord = theArray[i]
        if theArray[i] != "" and theArray[i] != "\n" and theArray[i] != "'":
            for i2 in range(0,len(theArray)):
                if theArray[i2] == tempWord:
                    theArray[i2] = ""
                    tempCount += 1
            print(tempCount,tempWord)
            theInfoArray.append([tempWord,tempCount])
        # theInfoArray now contains a WORD and NUMBER-OF-APPEARANCES: theInfoArray[data-point][0=Word|1=Appearances]
        # Now do a bubble sort moving the most the occurring words to the right most side!!!

    #=====================================================================================

    # OBJECTIVE 3 - Writing top 10 most used words to a CSV file
    # Bubble sort on a 2D array ASCENDING ORDER ***REPLACED WITH MORE EFFICIENT BUBBLE SORT
    topTen = [["",0],["",0],["",0],["",0],["",0],["",0],["",0],["",0],["",0],["",0]]
    temp = ["",0]
    temp[0] = theInfoArray[0][0]
    temp[1] = theInfoArray[0][1]
    index = 0

    for loop in range(0,10):
        for i in range(0,len(theInfoArray)):
            if theInfoArray[i][1] > temp[1]:
                temp[1] = theInfoArray[i][1]
                temp[0] = theInfoArray[i][0]
                index = i
        theInfoArray[index][1] = 0
        topTen[loop][0] = temp[0]
        topTen[loop][1] = temp[1]
        temp[1] = 0

    print(theInfoArray)
    print(alphabet)

    # OBJECTIVE 3 - Writing top 10 most used words to a CSV file
    # Following functions are used from "library csv" found @ and credit to https://docs.python.org/3/library/csv.html
    max = len(topTen)-1
    with open("test.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=" ",
                                quotechar="|", quoting=csv.QUOTE_MINIMAL)
        # Uses "max" to refer to the top value, max-1, max-2, ... used to refer to the next values
        writer.writerow([topTen[max-9][0]] + [topTen[max-9][1]])
        writer.writerow([topTen[max-8][0]] + [topTen[max-8][1]])
        writer.writerow([topTen[max-7][0]] + [topTen[max-7][1]])
        writer.writerow([topTen[max-6][0]] + [topTen[max-6][1]])
        writer.writerow([topTen[max-5][0]] + [topTen[max-5][1]])
        writer.writerow([topTen[max-4][0]] + [topTen[max-4][1]])
        writer.writerow([topTen[max-3][0]] + [topTen[max-3][1]])
        writer.writerow([topTen[max-2][0]] + [topTen[max-2][1]])
        writer.writerow([topTen[max-1][0]] + [topTen[max-1][1]])
        writer.writerow([topTen[max][0]] + [topTen[max][1]])

    #===================================================================================

    # OBJECTIVE 4 - Visually representing character frequency analysis via MATPLOTLIB

    # Following functions are used from "matplotlib"
    # found @ and credit to https://matplotlib.org/tutorials/introductory/pyplot.html

    # Plotting ALPHABET Characters
    alphabetNames = ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l"
            ,"M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z"]
    alphabetValues = alphabet
    plt.figure(figsize=(19.20, 10.80))
    plt.bar(alphabetNames, alphabetValues)
    plt.suptitle('Characters A-Z Upper and Lower Case Plotted')

    # Plotting PUNCTUATION Characters
    punctuationNames = ["space","newline","fullstop","comma","hyphen","ePoint","Qmark","apostrophe","elipses","colon",
                        "semi-colon"]
    punctuationValues = punctuation
    plt.figure(figsize=(19.20,10.80))
    plt.bar(punctuationNames,punctuationValues)
    plt.suptitle('Punctuation Characters Plotted')

    plt.show()

run()