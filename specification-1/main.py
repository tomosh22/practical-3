import csv
import matplotlib.pyplot as plt

def main():


    def parse():
        # OBJECTIVE 1 - Reading a text file and parsing the contents to a STRING and an ARRAY
        # User specifies text file and encoding. Specified file's content is parsed.
        print("1) Place a text file within the same directory as this python file.")
        print("\n2) Specify the file by inputting the name with the file extension.")
        filename = str(input("Enter filename: "))

        print("\n3) Specify the character set used within the text file.")
        print("|Recommended to use 'utf-8'|utf-8|ascii|utf-16|utf-32|")
        encoding = str(input("Enter character-set-encoding: "))

        try:
            quantityOfMostFrequent = -1
            print("\nNOTE: The most frequent words are written to a csv file named 'topWords.csv'.")
            while quantityOfMostFrequent <= 0:
                quantityOfMostFrequent = int(input("4) Enter desired quantity of most frequent words to be outputted: "))

            # Optional custom graph
            temp = ""
            choice = ""
            optionalLabels = []
            while choice != "Y" and choice != "y" and choice != "N" and choice != "n":
                print("\n5) OPTIONAL: Would you like to create a custom bar chart by specifying characters? (Y/N)")
                choice = str(input("Enter choice (Y/N): "))
                if choice == "Y" or choice == "y":
                    print("\nList of available characters: ")
                    print("[A,a,B,b,C,c,D,d,E,e,F,f,G,g,H,h,I,i,J,j,K,k,L,l,M,m,N,n,O,o,P,p,Q,q,R,r,S,s,T,t,U,u,V,v,W,w,X,x,Y,y,Z,z]")
                    print("IMPORTANT-INSTRUCTIONS: Input a single character from the list, then press enter, repeat until \n"
                          "you have entered all the characters you wish to display on your custom graph. To stop inputting characters type 'STOP'.")
                    while temp != "STOP":
                        temp = str(input("Enter a single character: "))
                        optionalLabels.append(temp)
            f = open(filename,"r",encoding=encoding)
            theString = f.read()

            countChars(theString, quantityOfMostFrequent, choice, optionalLabels)
        except FileNotFoundError:
            print("\nERROR: File not found, please try again.\n")
            parse()
        #except LookupError:
            #print("\nERROR: Encoding not found, please try again.\n")
            #parse()
        except UnicodeDecodeError:
            print("\nERROR: Incompatible encoding used, please try again with a different encoding.\n")
            parse()
        except ValueError:
            print("\nERROR: You must enter an integer value, to determine the quantity of most used words outputted.\n")
            parse()


    def countChars(theString, quantityOfMostFrequent, choice, optionalValues):
        # OBJECTIVE 2 - Frequency analysis of the characters within the text file using .count()
        # Counts the quantity of characters for letters and punctuation
        alphabet = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        countLetters = ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l",
        "M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z"]
        for i in range(0,len(alphabet)):
            alphabet[i] = theString.count(countLetters[i])

        punctuation = [0,0,0,0,0,0,0,0,0,0,0]
        countPunctuation = [" ","\n",".",",","-","!","?","'","...",":",";"]
        for i in range(0,len(punctuation)):
            punctuation[i] = theString.count(countPunctuation[i])

        removeUselessChars(theString, quantityOfMostFrequent)
        optionalPlot(choice, optionalValues, countLetters, alphabet, punctuation)

    def optionalPlot(choice, optionalLabels, countLetters, alphabet, punctuation):
        # Removes duplicates
        if choice == "Y" or choice == "y":
            for i in range(0,len(optionalLabels)):
                tempChar = optionalLabels[i]
                optionalLabels[i] = ""
                for i2 in range(0,len(optionalLabels)):
                    if tempChar == optionalLabels[i2]:
                        optionalLabels[i2] = ""
                    optionalLabels[i] = tempChar
        # Adds the character only if found in the "countLetters" array
            tempArray = optionalLabels
            optionalLabels = []
            optionalValues = []
            for i in range(0,len(tempArray)):
                for i2 in range(0,len(alphabet)):
                    if tempArray[i] == countLetters[i2]:
                        optionalLabels.append(tempArray[i])
                        optionalValues.append(alphabet[i2])
        # Plots the custom bar chart
            plot(alphabet, punctuation, optionalLabels, optionalValues)
        else:
            optionalLabels = []
            optionalValues = []
            plot(alphabet, punctuation, optionalLabels, optionalValues)

    def removeUselessChars(theString, quantityOfMostFrequent):
        print("PROGRESS: Removing redundant characters...")
        # Removes punctuation and replaces upper case with lower case letters for an accurate word count
        removePunc = [".", "?", "!", "...", ":", ";", ",","(",")","[","]","—","_","-","—“","“","”","‘","#","’","/"]
        for iremove in range(0,len(removePunc)):
            theString = theString.replace(removePunc[iremove],"")
        removeUpperCase = ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l"
                ,"M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z"]
        for iremove in range(0,len(removeUpperCase),2):
            theString = theString.replace(removeUpperCase[iremove],removeUpperCase[iremove+1])
        theArray = theString.split()
        wordCount(theArray, quantityOfMostFrequent)


    def wordCount(theArray, quantityOfMostFrequent):
        print("PROGRESS: Calculating quantity of each word...")
        # Counts each word, the word and count is stored within a 2D array
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
        BubbleSort(theInfoArray, quantityOfMostFrequent)


    def BubbleSort(theInfoArray, quantityOfMostFrequent):
        print("PROGRESS: Sorting to find the top most used words...")
        # OBJECTIVE 3 - Writing top 10 most used words to a CSV file
        # The 2D array storing words and quantity is bubble sorted
        theBubbleArray = theInfoArray
        topTen = []
        tempWord = theBubbleArray[0][0]
        tempCount = theBubbleArray[0][1]
        index = 0
        for loop in range(0,quantityOfMostFrequent):
                for i in range(0,len(theBubbleArray)):
                    if theBubbleArray[i][1] > tempCount:
                        tempWord = theBubbleArray[i][0]
                        tempCount = theBubbleArray[i][1]
                        index = i
                theBubbleArray[index][1] = 0
                if tempCount != 0:
                    topTen.append([tempWord,tempCount])
                tempCount = 0
        csvWrite(topTen)


    def csvWrite(topTen):
        print("PROGRESS: Writing top most used words to a CSV file")
        # OBJECTIVE 3 - Writing top 10 most used words to a CSV file
        # Following functions are used from "library csv"
        # found @ and credit to https://docs.python.org/3/library/csv.html

        # Quantity of most used words specified by user are written to the csv file
        with open("topWords.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=" ",
                                    quotechar="|", quoting=csv.QUOTE_MINIMAL)
            for i in range(0,len(topTen)):
                writer.writerow([topTen[i][0]] + [topTen[i][1]])


    def plot(alphabet, punctuation, optionalLabels, optionalValues):
        # OBJECTIVE 4 - Visually representing character frequency analysis via MATPLOTLIB
        # Following functions are used from "matplotlib"
        # found @ and credit to https://matplotlib.org/tutorials/introductory/pyplot.html

        # Character analysis for letters and punctuation is plotted
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

        if optionalLabels != []:
            plt.figure(figsize=(19.20,10.80))
            plt.bar(optionalLabels,optionalValues)
            plt.suptitle('User-Specified Characters')

        plt.show()

    parse()

main()

# ADD 2 FEATURES
# Choose characters to plot
# Show progress through print messages

