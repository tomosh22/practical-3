import csv
import matplotlib.pyplot as plt

def main():
    def parse():
        # OBJECTIVE 1 - Reading a text file and parsing the contents to a STRING and an ARRAY
        # User specifies text file and encoding. Specified file's content is parsed.
        print("1) Place a text file within the same directory as this python file")
        print("2) Specify the file by inputting the name with the file extension")
        filename = str(input("Enter filename: "))
        print("NOTE: Top ten words are written to a csv file named 'topten.csv'.")
        print("3) Specify the character set used within the text file you wish to use")
        print("|Recommended to use 'utf-8'|utf-8|ascii|utf-16|utf-32|")
        encoding = str(input("Enter character-set-encoding: "))
        f = open(filename, "r", encoding=encoding)
        try:
            f = open(filename,"r",encoding=encoding)
        except FileNotFoundError:
            print("\nERROR: File not found, please try again.\n")
            parse()
        except LookupError:
            print("\nERROR: Encoding not found, please try again.\n")
            parse()
        theString = f.read()
        countChars(theString)

    def countChars(theString):
        # OBJECTIVE 2 - Frequency analysis of the characters within the text file using .count()
        # Counts letters and punctuation
        alphabet = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        countLetters = ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l",
        "M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z"]
        for i in range(0,len(alphabet)):
            alphabet[i] = theString.count(countLetters[i])

        punctuation = [0,0,0,0,0,0,0,0,0,0,0]
        countPunctuation = [" ","\n",".",",","-","!","?","'","...",":",";"]
        for i in range(0,len(punctuation)):
            punctuation[i] = theString.count(countPunctuation[i])

        removeUselessChars(theString)
        plot(alphabet, punctuation)

    def removeUselessChars(theString):
        # Removes punctuation and replaces upper case with lower case letters for an accurate word count
        removePunc = [".", "?", "!", "...", ":", ";", ",","(",")","[","]","—","_","-","—“","“","”","‘","#","’","/"]
        for iremove in range(0,len(removePunc)):
            theString = theString.replace(removePunc[iremove],"")
        removeUpperCase = ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l"
                ,"M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z"]
        for iremove in range(0,len(removeUpperCase),2):
            theString = theString.replace(removeUpperCase[iremove],removeUpperCase[iremove+1])
        theArray = theString.split()
        wordCount(theArray)

    def wordCount(theArray):
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
        print(theInfoArray)
        BubbleSort(theInfoArray)

    def BubbleSort(theInfoArray):
        # OBJECTIVE 3 - Writing top 10 most used words to a CSV file
        # The 2D array storing words and quantity is bubble sorted but only the top ten elements for efficiency
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
        csvWrite(topTen)

    def csvWrite(topTen):
        # OBJECTIVE 3 - Writing top 10 most used words to a CSV file
        # Following functions are used from "library csv"
        # found @ and credit to https://docs.python.org/3/library/csv.html
        # Top ten words are written to a csv file
        max = len(topTen)-1
        with open("topten.csv", "w", newline="") as csvfile:
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

    def plot(alphabet, punctuation):
        # OBJECTIVE 4 - Visually representing character frequency analysis via MATPLOTLIB
        # Following functions are used from "matplotlib"
        # found @ and credit to https://matplotlib.org/tutorials/introductory/pyplot.html
        # Character analysis is plotted
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

    parse()

main()

