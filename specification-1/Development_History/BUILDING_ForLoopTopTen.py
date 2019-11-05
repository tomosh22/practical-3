the2Darray = [["the",2108],["in",353],["where",1323],["she",242],["higher",442],["nope",3824],["yes",524],["trigger",2],
              ["sixty",8439],["long",294],["rising",847],["pheonix",454],["never",1],["surrender",1],["int",231],
              ["love",8346],["name",9999],["for",3812],["leave",328],["magic",83],["ironman",48],["btw",89],["find",20],
              ["i",834],["newcastle",489]]

topTen = [["",0],["",0],["",0],["",0],["",0],["",0],["",0],["",0],["",0],["",0]]

temp = ["",0]
temp[0] = the2Darray[0][0]
temp[1] = the2Darray[0][1]
index = 0

for loop in range(0,10):
    for i in range(0,len(the2Darray)):
        if the2Darray[i][1] > temp[1]:
            temp[1] = the2Darray[i][1]
            temp[0] = the2Darray[i][0]
            index = i
    the2Darray[index][1] = 0
    topTen[loop][0] = temp[0]
    topTen[loop][1] = temp[1]
    temp[1] = 0

print(the2Darray)
print(topTen)

'''When the program is counting up the words from the first array created it temporarily stores the words and quantity 
before placing it in an array. It may be possible to skip placing it in an array and instead simply store the top ten 
words as the array is being created.'''

#A person can decide the upper limit of the loop named "loop" to decide the quantity of most used words available