# How to use Program
0) This program returns the quantity of each character A to Z and the most used words within a text file
1) Firstly place a text file you wish to be analysed within the folder named "specification-1"
2) A prompt will ask you to enter the file's name, this includes the name and extension to be inputted
3) Each text file uses a character set, enter the name of the character set used within your text file
4) This program will write the most used words to a csv file, you will be prompted to specify the number of words to be written
5) a) You may or may not create a custom graph if you wish to simply type in "y" or "Y"
5) b) Upon doing so you will see a list of characters you can specify to be plotted on your custom graph
5) c) Simply type in a single character within the prompt, like so "Enter a single character: f"
5) d) Then press enter, the same prompt will re-appear "Enter a single character:"
5) e) From here either type another character you wish to see on your custom graph
5) f) Or type "STOP" and then program will proceed to create the default graph along with your custom graph
5) g) Inputting invalid characters will simply be filtered out instead of the program crashing

## Produce a Markdown file in your repository directory that combines your findings in one place.

### 1 Read in a .txt file and parse the content.
From previous experience during A-level I knew that I could use the method ".open()" in order to retrieve data from  
a text file. However at the time of doing this, I was not using the provided text document but instead my own created  
text files. As a result, near the end of development for this program, when I discovered the provided text document  
it did not work on the first try. This caused me to have to learn something new, which is, the encoding can be specified with the  
.open() method, such that when a text file is opened the characters within the text file are from a certain character  
set, the corresponding character set must be specified in order to validly parse the contents, hence, the encoding.  
Within this section the user must specify the text file's name and encoding, I used try-catch-exceptions so that if the  
user enters incorrect data the program simply starts again. This is true if the user enters an incompatible encoding with a  
text file, the program no longer crashes it simply returns an error message and starts the program again. This is also  
true if the user enters an encoding set that does not exist or text file name that does not exist. 

### 2 Perform a frequency analysis of the characters and words in the text file.

In order for my program to perform a frequency analysis of the characters I simply used .count() to assign  
the quantity of a specified letter to values in an array to be later used for plotting, this extends to all upper  
and lower case letters, along with punctuation.  
Interestingly, the program treats "right" and "right." as two different words because of the full-stop in the  
second word. This needed to be fixed as it was leading to inaccurate word counts. Hence the next block of code  
removes most punctuation, some are not removed due to them being apart of the word i.e "can't". This behaviour of  
inaccurate word counts also applies to upper and lower case letters such that "Right" and "right" are also different.  
Therefore upper-case letters had to be replaced with lower case letters - this is achieved by using an array of upper  
and lower case letters, the for loop only looks at upper case letters by incrementing by 2 each time so if a character  
in the string matches a character specified by the for loop, the character is always replaced with the corresponding 
lowercase character.  
The next step is, punctuation, this is simply replaced with nothing. Once these two steps have been executed a new array is then derived    
from this string, which contains each word as an element of the new array. Using .split() to achieve this.  
Lastly a word count is executed using the new array containing each word, this is achieved by using a nested for  
loop. Which firstly selects the word, then iterates through the entire array increasing a counter each time the same  
 word is found. This counter and the word being counted, when the nested for loop has finished searching for  
duplicates the word and count is then added to a 2D array to be manipulated later in the program. 

### 3 Output the frequency of the most occurring words in the text file to a CSV file.
To write the most frequent words to a CSV file I first needed a way of calculating the most frequent words.  
Since each unique word and word-count was stored in a 2D array I could simply use a bubble sort on the whole 2D array.  
However this proved extremely inefficient, I was only writing the top ten most used words to a CSV file, hence I limited  
the bubble sort to ten items which is much more faster than sorting the whole 2D array.  
When it came to writing the top ten most used words, I simply used a CSV library, to write the top ten words. 

### 4 Present your frequency analysis of the characters visually using the Matplotlib plotting library.
Lastly presenting the frequency analysis. This was very simple at first, however I ran into a problem which I learned  
quite a bit from. At the time whenever I ran the "ObjectivesMet4.py" which plots the punctuation, the "comma"s return value is  
incorrect this is evident because when this is ran on the text file I wrote, it returns 255 "commas" despite there being only 1.  
Furthermore when this is run on the STAR WARS script it returns around 30,000 "commas" which is also wrong. Interestingly,  
upon removing the "count" for "commas" the error then moves onto "full stops". Upon further investigation the bug was tracked  
all the way back to version "ObjectivesMet2.py" Another step I took, was to determine a fact, is this problem also within the alphabet  
characters or only in the punctuation characters. To determine this fact, I separated alphabet-character and punctuation-characters  
into different arrays. Then checked if the values for each element of each array is correct. Upon doing so I realized that   
1 ~ When I told the program to count spaces, it was not, this is because I did not specify to count spaces, but instead  
to count "nothing". Within the code I put [count("")] instead of [count(" ")] the latter is correct because I should be  
counting white spaces, not "nothing". 2 ~ when it came to plotting, the visual graph itself relies on the order of names  
and order of integer values to be in the corresponding order such that when plotting data, the names and values are plotted  
separately like so: names = [column1, column2, column3,...] values = [14,15,16] the value 14 will be plotted with the name  
"column1", value 15 will be plotted with the name "column2" and so on, the data is plotted according to equal index values.  
What I was doing wrong, was that, in my names array "space" came first, but in my values array "fullstops" came first,  
hence the number of fullstops were being plotted for spaces. Therefore the "30,000 commas" value must have come about from  
"nothing" being counted instead of "spaces" and combined with the "names" and "values" array being out of order it appeared  
that 30,000 commas were being counted, but in fact 30,000 "nothing" were being counted and displayed under commas.  

