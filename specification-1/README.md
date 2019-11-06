###1 Read in a .txt file and parse the content.
From previous experience during A-level I knew that I could use the method ".open()" in order to retrieve data from  
a text file. However at the time of doing this, I was not using the provided text document but instead my own created  
text files. As a result, near the end of development for this program, when I discovered the provided text document  
it did not work on the first try. This caused me to have to learn something new, which is, the encoding can be specified with the  
.open() method, such that when a text file is opened the characters within the text file are from a certain character  
set, the corresponding character set must be specified in order to validly parse the contents, hence, the encoding.  
Within this section the user must specify the text file's name and encoding, I used try-catch-exceptions so that if the  
user enters incorrect data the program simply starts again. However this is not true if the user enters an  
incompatible encoding with a text file, the program crashes - this is because a try-catch-exception cannot be used in  
this case because an error is not returned from the line of code within the try-catch-exception that is executed,  
but instead the error is returned from another python file where the character set is contained separate from my own  
creation. Lastly the contents of the text file is stored within a string for later manipulation.

###2 Perform a frequency analysis of the characters and words in the text file.

In order for my program to perform a frequency analysis of the characters I simply used .count() to assign  
the quantity of a specified letter to a variable name that corresponds to the character it tracks, for all upper  
and lower case letters, along with punctuation.  
Interestingly, the program treats "right" and "right." as two different words because of the full-stop in the  
second word. This needed to be fixed as it was leading to inaccurate word counts. Hence the next block of code  
removes most punctuation, some are not removed due to them being apart of the word i.e "can't". This behaviour of  
inaccurate word counts also applies to upper and lower case letters such that "Right" and "right" are also different.  
Therefore upper-case letters had to be replaced with lower case letters - how this is achieved is explained as a  
multi-line comment within the code itself. Once these two steps have been executed a new array is then derived    
from this array, which contains each word as an element of the new array. Using .split() to achieve this.  
Lastly a word count is executed using the new array containing each word, this is achieved by using a nested for  
loop. Which firstly selects the word, then iterates through the entire array increasing a counter each time a  
duplicate word is found. This counter and the word being counted when the nested for loop has finished searching for  
duplicates is then added to another 2D array to then be manipulated later in the program. 

###3 Output the frequency of the most occurring words in the text file to a CSV file.
To write the most frequent words to a CSV file I first needed a way of calculating the most frequent words.  
Since each unique word and word-count was stored in a 2D array I could simply use a bubble sort on the whole 2D array.  
However this proved extremely inefficient, I was only writing the top ten most used words to a CSV file, hence I limited  
the bubble sort to ten items which is much more faster than sorting the whole 2D array.  
When it came to writing the top ten most used words, I simply used a CSV library, to write the top ten words. 

###4 Present your frequency analysis of the characters visually using the Matplotlib plotting library.

Lastly presenting the frequency analysis. This was very simple as I only ran into one problem which  
is explained in much more detail within "_Notes" (the first paragraph). The documentation is very  
simple and easy to follow, I took an example and some other functions and produced the bar chart.
However I learned that when plotting information, I learned that when specifying the names and  
the values to be plotted, the names and values placement or index must correspond otherwise values  
will be plotted against incorrect names. 
