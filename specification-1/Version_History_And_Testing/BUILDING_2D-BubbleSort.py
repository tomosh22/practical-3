# Create a bubble sort, resulting in the list being modified to ascending order <smallest-Largest>
theInfoArray = [["the",10],["fish",15],["bubble",8],["stumped",11],["unary",4],["binary",2],["ternary",6]]

        # OBJECTIVE 3 - Writing top 10 most used words to a CSV file
        # The 2D array storing words and quantity is bubble sorted, but only the top ten elements for efficiency
quantityOfMostFrequent = int(input("Enter the number of most used words to be written to a CSV file: "))
theBubbleArray = theInfoArray
topTen = []
tempWord = theBubbleArray[0][0]
tempCount = theBubbleArray[0][1]
index = 0
for loop in range(0,quantityOfMostFrequent):
        for i in range(0,len(theBubbleArray)):
            print(theBubbleArray[i][1], tempCount)
            if theBubbleArray[i][1] > tempCount:
                tempWord = theBubbleArray[i][0]
                tempCount = theBubbleArray[i][1]
                index = i
        theBubbleArray[index][1] = 0
        if tempCount != 0:
            topTen.append([tempWord,tempCount])
        else:
            print("Upper limit has been reached")# Call next function (the limit has been reached)
        tempCount = 0

print(topTen)



'''
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
'''


