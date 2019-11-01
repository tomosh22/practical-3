# Create a bubble sort, resulting in the list being modified to ascending order <smallest-Largest>
theInfoArray = [["the",10],["fish",15],["bubble",8],["stumped",11],["unary",4],["binary",2],["ternary",6]]
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



