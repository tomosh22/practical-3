import csv
import matplotlib.pyplot as plt

def parse():
    # OBJECTIVE 1 - Reading a text file and parsing the contents to a STRING and an ARRAY
    print("1) Place a text file within the same directory as this python file")
    print("2) Specify the file by inputting the name with the file extension")
    filename = str(input("Enter filename: "))
    print("3) Specify the character set used within the text file you wish to use")
    print("|Recommended to use 'utf-8'|utf-8|ascii|utf-16|utf-32|")
    encoding = str(input("Enter character-set-encoding: "))
    try:
        f = open(filename,"r",encoding=encoding)
    except FileNotFoundError:
        print("\nERROR: File not found, please try again.\n")
        parse()
    except LookupError:
        print("\nERROR: Encoding not found, please try again.\n")
        parse()
    theString = f.read()
    return(theString)
    #=====================================================================================

def countChars(theString):
    # OBJECTIVE 2 - Frequency analysis of the characters within the text file using .count()
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
    return alphabet, punctuation

def removeUselessChars(theString):
    removePunc = [".", "?", "!", "...", ":", ";", ",","(",")","[","]","—","_","-","—“","“","”","‘","#"]
    for iremove in range(0,len(removePunc)):
        theString = theString.replace(removePunc[iremove],"")
    removeUpperCase = ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l"
            ,"M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z"]
    # 0 = UpperA, 1 = LowerA, 2 = UpperB, 3 = LowerB THEREFORE (Even-Index = Upper) AND (Odd-Index = Lower)
    for iremove in range(0,len(removeUpperCase),2):
        theString = theString.replace(removeUpperCase[iremove],removeUpperCase[iremove+1])
    theArray = theString.split()
    return theArray

def wordCount(theArray):
    theInfoArray = []
    for i in range(0,len(theArray)):
        tempCount = 0
        tempWord = theArray[i]
        if theArray[i] != "" and theArray[i] != "\n" and theArray[i] != "'":
            for i2 in range(i,len(theArray)):
                if theArray[i2] == tempWord:
                    theArray[i2] = ""
                    tempCount += 1
            theInfoArray.append([tempWord,tempCount])
    return theInfoArray

    #=====================================================================================

def BubbleSort(theInfoArray):
    # OBJECTIVE 3 - Writing top 10 most used words to a CSV file
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
    return topTen

def csvWrite(topTen):
    # OBJECTIVE 3 - Writing top 10 most used words to a CSV file
    # Following functions are used from "library csv" found @ and credit to https://docs.python.org/3/library/csv.html
    max = len(topTen)-1
    with open("test.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=" ",
                                quotechar="|", quoting=csv.QUOTE_MINIMAL)
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

    alphabetNames = ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l"
            ,"M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z"]
    alphabetValues = alphabet
    plt.figure(figsize=(19.20, 10.80))
    plt.bar(alphabetNames, alphabetValues)
    plt.suptitle('Characters A-Z Upper and Lower Case Plotted')

    punctuationNames = ["space","newline","fullstop","comma","hyphen","ePoint","Qmark","apostrophe","elipses","colon",
                        "semi-colon"]
    punctuationValues = punctuation
    plt.figure(figsize=(19.20,10.80))
    plt.bar(punctuationNames,punctuationValues)
    plt.suptitle('Punctuation Characters Plotted')

    plt.show()

run()
