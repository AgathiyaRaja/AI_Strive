#!/usr/bin/env python
# coding: utf-8

# # Intro to Python - Exercises - Part 6

# ## 6. Strings

# Until now, most examples and exercises have been using numbers. In daily life, it is far more commonplace to deal with textual information. So are you ever going to learn how to deal with texts?
# 
# The reason that dealing with texts was postponed until this point, is that dealing with numbers is simply easier than dealing with texts. But in the present section, the first steps are taken to learn to manipulate textual information.
# 
# Texts, in programming languages, are dealt with in the form of strings. This section is on the details of strings, and on readily-available functions to juggle them.

# ### Multi-line strings

# Strings in Python may span across multiple lines. This can be useful when you have a very long string, or when you want to format the output of the string in a certain way. Multi-line strings can be achieved in two ways:
# 
# 1. With single or double quotes, and an indication that the remainder of the string continues on the next line with a backslash.
# 2. With triple single or double quotes.
# 
# I first demonstrate how this works when you use the regular string enclosure with one double or single quote at each end of the string:

# In[1]:


longString = "I'm fed up with being treated like sheep. What's the point of going abroad if you're just another tourist carted around in buses surrounded by sweaty mindless oafs from Kettering and Coventry in their cloth caps and their cardigans and their transistor radios and their Sunday Mirrors, complaining about the tea - 'Oh they don't make it properly here, do they, not like at home' - and stopping at Majorcan bodegas selling fish and chips and Watney's Red Barrel and calamaris and two veg and sitting in their cotton frocks squirting Timothy White's suncream all over their puffy raw swollen purulent flesh 'cos they 'overdid it on the first day."
print(longString)


# As you can see, Python now interprets this example as a single line of text. The backslash (`\`) can actually be included after any Python statement to indicate that it continues on the next line, and it can be quite useful for that, for instance when you write long calculations.
# 
# The recommended way to write multi-line strings in Python is, however, to use triple double or single quotes. I indicated earlier that you can use those to write multi-line comments. Such comments are basically large strings in the middle of your Python program, which do nothing as they are not assigned to a variable.
# 
# Here is an example of a long string with triple double quotes:

# In[2]:


longString = """And being herded into endless Hotel Miramars and Bellevueses 
and Continentales with their modern international luxury 
roomettes and draught Red Barrel and swimming pools full 
of fat German businessmen pretending they're acrobats forming 
pyramids and frightening the children and barging into queues 
and if you're not at your table spot on seven you miss the 
bowl of Campbell's Cream of Mushroom soup, the first item on 
the menu of International Cuisine, and every Thursday night 
the hotel has a bloody cabaret in the bar, featuring a tiny 
emaciated dago with nine-inch hips and some bloated fat tart 
with her hair brylcreemed down and a big arse presenting 
Flamenco for Foreigners."""
print(longString)


# The interesting difference between these two examples is that in the first example, the string was interpreted as one long, continuous series of characters, while in the second example the different lines are all printed on different lines on the output. The reason that this happens is that there is an invisible character included at the end of each line in the second example that indicates that Python should move to the next line before continuing. This is the so-called "newline" character, and you can actually insert it explicitly into a string, using the code "`\n`". So this code should not be read as two characters, the backslash and the "n", but as a single newline character. By using it, you can ensure that you print the output on multiple lines, even if you use the backslash to indicate the continuation of the string, as was done in the first example. For example:

# In[3]:


longstring = "And then some adenoidal typists from Birmingham with flabby\nwhite legs and diarrhoea trying to pick up hairy bandy-legged\nwop waiters called Manuel and once a week there's an excursion\nto the local Roman Ruins to buy cherryade and melted ice cream\nand bleeding Watney's Red Barrel and one evening you visit the\nso called typical restaurant with local colour and atmosphere\nand you sit next to a party from Rhyl who keep singing\n'Torremolinos, torremolinos' and complaining about the food -\n'It's so greasy here, isn't it?' - and you get cornered by some\ndrunken greengrocer from Luton with an Instamatic camera and\nDr. Scholl sandals and last Tuesday's Daily Express and he\ndrones on and on and on about how Mr. Smith should be running\nthis country and how many languages Enoch Powell can speak and\nthen he throws up over the Cuba Libres."
print(longstring)


# This means that if you do not want automatic newline characters inserted into a multi-line string, you have to use the first approach, with the backslash at the end of the line. If you are okay with newline characters in your multi-line string, the second approach is probably the easiest to read.

# ### Escape sequences

# "`\n`" is a so-called "escape sequence". An escape sequence is a string character written as a backslash followed by a code, which can be one or multiple characters. Python interprets escape sequences in a string as a special character; a control character.

# In[4]:


word1 = "orange"
word2 = "banana"

def add_newline_between_words(word1,word2):
    new_line = word1 + "\n" + word2
    return(new_line)
    
print(add_newline_between_words(word1,word2))


# Besides the newline character there are more special characters "`\'`" and "`\"`", which can be used to place a single respectively double quote in a string, regardless of what characters surround the string. I also mentioned that you can use "`\\`" to insert a "real" backslash in a string. 
# 
# There are a few more "backslash sequences" which lead to a special character. Most of these are archaic and you do not need to worry about them. The one I want to mention are "`\t`" which represents a single tabulation (also known as the 'tab').

# In[5]:


d = "test"
m = "me" 

def place_word_between_single_quotes(w1):
    new_line = '\'' + word1 + "\'"
    return(new_line)
print(place_word_between_single_quotes(m))


def place_word_between_double_quotes(w1):
    new_line = '\t' + word1 + '"'
    return(new_line)
print(place_word_between_double_quotes(d))


# Extra information for students who want to know more, but not necessary for this course:
# 
# There is another character "`\xnn`" whereby `nn` stands for two hexadecimal digits, which represents the character with hexadecimal number `nn`. For example, "`\x20`" is the character expressed by the hexadecimal number `20`, which is the same as the decimal number `32`, which is the space (this will be explained later in this chapter).
# 
# In case you never learned about hexadecimal counting: hexadecimals use a numbering scheme that uses 16 different digits. We use ten (`0` to `9`), binary uses two (`0` to `1`), and hexidecimal then uses `0` to `9` and then continues from `A` to `F`. A direct translation from hexadecimals to decimals turns `A` into `10`, `B` into `11`, etcetera. In decimal counting, the value of a multi-digit number is found by multiplying the digits by increasing powers of `10`, from right to left, e.g., the number `1426` is `6 + 2*10 + 4*100 + 1*1000`. For hexadecimal numbers you do the same thing, but multiply by powers of `16`, e.g., the hexadecimal number `4AF2` is `2 + 15*16 + 10*256 + 4*4096`. Programmers tend to like hexadecimal numbers, as computers work with bytes as the smallest unit of memory storage, and a byte can store 256 different values, i.e., any byte value can be expressed by a hexadecimal number of two digits. 

# ### Accessing characters of a string

# As I showed several times before, a string is a collection of characters in a specific order. You can access the individual characters of a string using indices.

# ### String indices

# Each symbol in a string has a position, this position can be referred to by the index number of the position. The index numbers start at 0 and then increase to the length of the string. The following table shows the word "orange" in the first row and the indices for each letter in the second and third rows:
# 
# &nbsp;&nbsp;__`  o  r  a  n  g  e`__<br>
# &nbsp;&nbsp;`  0  1  2  3  4  5`<br>
# ` -6 -5 -4 -3 -2 -1`
# 
# As you can see, you can use positive indices, which start at the first letter of the string and increase until the end of the string is reached, or negative indices, which start with -1 for the last letter of the string and decrease until the first letter of the string is reached.
# 
# As the length of a string `s` is `len(s)`, the last letter of the string has index `len(s)-1`. With negative indices, the first letter of the string has index `-len(s)`.
# 
# If a string is stored in a variable, the individual letters of the string can be accessed by the variable name and the index of the requested letter between square brackets (`[]`) next to it.

# In[6]:


fruit = "orange"

def print_indices(fruit,n):
    print(fruit[n])
    
print_indices(fruit,1) 
print_indices(fruit,2) 
print_indices(fruit,4)
print_indices(fruit,-1)
print_indices(fruit,-6)
print_indices(fruit,-3)


# Besides using single indices you can also access a substring (also called a "slice") from a string by using two numbers between the square brackets with a colon (`:`) in between. The first of these numbers is the index where the substring starts, the second where it ends. The substring does *not* include the letter at the second index. By leaving out the left number you indicate that the substring starts at the beginning of the string (i.e., at index 0). By leaving out the right number you indicate that the substring ranges up to and includes the last character of the string.
# 
# If you try to access a character using an index that is beyond the reaches of a string, you get a runtime error ("index out of bounds"). For a range of indices to access substrings such limitations do not exist; you can use numbers that are outside the bounds of the string.

# In[7]:


fruit = "orange"
print(fruit[:])
print(fruit[0:])
print(fruit[:5])
print(fruit[:100])
print(fruit[:len(fruit)])
print(fruit[1:-1])
print(fruit[2], fruit[1:6])


# ### Traversing strings

# We already saw how you can traverse the characters of a string using a `for` loop:

# In[8]:


fruit = 'apple'

def traverse_characters(word):
    new_word = ""
    for char in word:
        new_word+=(char + ' - ')
    return new_word
print(traverse_characters(fruit))


# Now you know about indices, you probably realize you can also use those to traverse the characters of a string:

# In[9]:


fruit = 'apple'

def traverse_characters2(word):
    new_word = ""
    for i in range(0, len(word)):
        new_word += word[i] + " - "
    return new_word       
    
def traverse_characters3(word):                            
    new_word = ""
    i = 0
    while i < len(word):
        new_word += word[i] + " - "
        i += 1
    return new_word

print(traverse_characters2(fruit)+"\n"+traverse_characters3(fruit))


# If you just want to traverse the individual characters of a string, the first method, using `for <character> in <string>:`, is by far the most elegant and readable. However, occasionally you have to solve problems in which you might prefer one of the other methods.
# 
# **Exercise (optional)**: Write code that for a string prints the indices of all of its vowels (`a`, `e`, `i`, `o`, and `u`). This can be done with a `for` loop or a `while` loop.

# In[10]:


# Indices of vowels
def index_vowels (text):

    
index_vowels("apple")


# **Exercise (optional)**: Write code that uses two strings. For each character in the first string that has exactly the same character at the same index in the second string, you print the character and the index. Watch out that you do not get an "index out of bounds" runtime error.

# In[11]:


# Your function
s1 = "The Holy Grail"
s2 = "Life of Brian"

def similar_char(text1, text2):


        
print(similar_char(s1, s2))


# **Exercise (optional)**: Write a function that takes a string as argument, and creates a new string that is a copy of the argument, except that every non-letter is replaced by a space (e.g., "`ph@t l00t`" is changed to "`ph t l  t`"). To write such a function, you will start with an empty string, and traverse the characters of the argument one by one. When you encounter a character that is acceptable, you add it to the new string. When it is not acceptable, you add a space to the new string. Note that you can check whether a character is acceptable by simple comparisons, e.g., any lower case letter can be found using the test `if ch >= 'a' and ch <= 'z':`. 

# In[12]:


# String cleaning function
def clean_string(string):
  

clean_string("Aph@t 100t")


# ### Extended slices

# Slices (substrings) in python can take a third argument, which is the step size (or "stride") that is taken between indices. It is similar to the third argument for the `range()` function. The format for slices then becomes `<string>[<begin>:<end>:<step>]`. By default the step size is 1.
# 
# The most common use for the step size is to use a negative step size in order to create a reversed version of a string.

# In[13]:


fruit = "banana"
print(fruit[::2])
print(fruit[1::2])
print(fruit[::-1]) 
print(fruit[::-2]) 


# Reversing a string using `[::-1]` is conceptually similar to traversing the string from the last character to the beginning of the string using backward steps of size 1.

# In[14]:


fruit = "banana"                
for i in range(len(fruit), -1):
    print(fruit[i])   


# ### Strings are immutable

# A core property of strings is that they are *immutable*. This means that they cannot be changed. For instance, you cannot change a character of a string by assigning a new value to it. As a demonstration, the following code leads to a runtime error if you try to run it:

# In[15]:


fruit = "oringe"
fruit[2] = "a"
print(fruit)


# If you want to make a change to a string, you have to create a new string that contains the change; you can then assign the new string to the existing variable if you want. For instance:

# In[16]:


fruit = "oringe"
fruit = fruit[:2] + "a" + fruit[3:]
print(fruit)


# The reasons for why strings are immutable are beyond the scope of this course. Just remember that if you want to modify a string you need to overwrite the entire string, and you cannot modify individual indices.

# ### `string` methods

# There is a collection of methods that are designed to operate on strings. All of these methods are applied to a string to perform some operation. Since strings are immutable, they *never change* the string they work on, but they always `return` a changed version of the string.
# 
# All these methods are called as `<string>.<method>()`, i.e., you have to write the string that they work on before the method call, with a period in between. You will encounter this more often, and why this is implemented in this way will be explained later in the course, in the chapters about object orientation.
# 
# Most of these methods are not part of a specific module, but can be called without importing them. There is a `string` module that contains specific constants and methods that can be used in your programs, but the methods I discuss here can all be used without importing the `string` module.

# ### `strip()`

# `strip()` removes from a string leading and trailing spaces, including leading and trailing newlines and other characters that may be viewed as spaces. There are no parameters. See the following example (the string is bordered by [ and ] to show the effect):

# In[17]:


s = "    And now for something completely different\n     "
print("["+s+"]")
s = s.strip()
print("["+s+"]")


# ### `upper()` and `lower()`

# `upper()` creates a version of a string of which all letters are capitals. `lower()` is equivalent, but uses only lower case letters. Neither method uses parameters.

# In[18]:


s = "The Meaning of Life"
print(s)
print(s.upper())
print(s.lower())


# ### `find()`

# `find()` can be used to search in a string for the starting index of a particular substring. As parameters it gets the substring, and optionally a starting index to search from, and an ending index. It returns the lowest index where the substring starts, or `-1` if the substring is not found.

# In[19]:


s = "Humpty Dumpty sat on the wall"
print(s.find("sat"))
print(s.find("t"))
print(s.find("t", 12))
print(s.find("q"))

s.find(" ")


# ### `replace()`

# `replace()` replaces all occurrences of a substring with another substring. As parameters it gets the substring to look for, and the substring to replace it with. Optionally, it gets a parameter that indicates the maximum number of replacements to be made. 
# 
# I must stress again that strings are immutable, so the `replace()` function is not actually changing the string. It returns a new string that is a copy of the string with the replacements made.

# In[20]:


s = ' Humpty Dumpty sat on the wall '
new_s = s.replace('sat on', 'fell off') 

print(new_s)
print(s)


# ### `split()`

# `split()` splits a string up in words, based on a given character or substring which is used as separator. The separator is given as the parameter, and if no separator is given, the white space is used, i.e., you split a string in the actual words (though punctuation attached to words is considered part of the words). If there are multiple occurrences of the separator next to each other, the extra ones are ignored (i.e., with the white space as separator, it does not matter if there is a single white space between two words, or multiple).
# 
# The result of this split is a so-called "list" of strings. Lists are discussed in a coming chapter. However, note that if you want to access the separate words, you can use the `for <word> in <list>:` construction.

# In[21]:


s = 'Humpty Dumpty sat on the wall'
wordlist = s.split()
for i in wordlist:
    print(i)
print(wordlist)


# A very useful property of splitting is that we can decode some basic file formats. For example, a comma separated value (CSV) file is a very simple format, of which the basic setup is that each line consists of values that are separated by a comma. These values can be split from each other using the `split()` method. (Note: In actuality it will be a bit more convoluted as there might be commas in the fields that are stored in the CSV file, so it depends a bit on the contents of the file whether this simple approach will work. More on CSV files will be said in a later chapter in the course, where file formats are discussed.)

# In[22]:


csv = "2016,September,28,Data Processing,Tilburg University,Tilburg"
values = csv.split(',')
for value in values:
    print(value)

print("")
print(values)
print (values[1][0])


# ### `join()`

# `join()` is the opposite of `split()`. `join()` joins a list of words together, separated by a specific separator. This sounds like it would be a method of lists, but for historic reasons it is defined as a string method. Since all string methods are called with the format `<string>.<method>()`, there must be a string in front of the call to `join()`. That string is the separator that you want to use, while the parameter of the method is the list that you want to join together. The return value, as always, is the resulting string. In the following example, note the notation of each of these steps:

# In[23]:


s = "Humpty;Dumpty;sat;on;the;wall"
print (s)
wordlist = s.split(';')
print (wordlist)
s = " ".join(wordlist)
print(s)


# ### What you learned

# In this chapter, you learned about:
# 
# - Strings
# - Multi-line strings
# - Accessing string characters with positive and negative indices
# - Slices
# - Immutability of strings
# - String methods `strip()`, `upper()`, `lower()`, `find()`, `replace()`, `split()`, and `join()`
# - Escape sequences

# # Exercises

# **Exercise 6.1:** The text string in the next cell contains several words which are enclosed by square brackets (`[` and `]`). Scan the string and print out all words which are between square brackets. For example, if the text string would be "`[a]n example[ string]`", you are expected to print out "`a string`".

# In[25]:


# Distilling text.


# **Exercise 6.2:** Print a line of all the capital letters "A" to "Z". Below it, print a line of the letters that are 13 positions in the alphabet away from the letters that are above them. E.g., below the "A" you print an "N", below the "B" you print an "O", etcetera. You have to consider the alphabet to be circular, i.e., after the "Z", it loops back to the "A" again.

# In[26]:


# ROTR-13


# **Exercise 6.3:** In the text below, count how often the word "wood" occurs (using program code, of course). Capitals and lower case letters may both be used, and you have to consider that the word "wood" should be a separate word, and not part of another word. Hint: If you did the exercises from this chapter, you already developed a function that "cleans" a text. Combining that function with the `split()` function more or less solves the problem for you.

# In[1]:


text = """How much wood would a woodchuck chuck
If a woodchuck could chuck wood?
He would chuck, he would, as much as he could,
And chuck as much as a woodchuck would
If a Mr. Smith could chuck wood\n\r\t."""

# read whole text
# create a counter
# get rid \n
# get rid of ?. special grammar
# lowercase my sentence
"if a woodchuck could chuck wood"
# split the string by some character
["if", "a", "woodchuck"]
#check if wood is in the list
    # if yes
       # counter = counter +1 <--> counter += 1 
    # else
        #pass
#return
        


# In[13]:


# Counting wood.
def wood_counter(text):
    text = text.replace("?", "").replace(".","")
    l = text.lower().strip().split()
    counter = 0
    for word in l:
        if word == "wood":
            counter +=1
    return counter
wood_counter(text)


# In[14]:


help(str)


# In[ ]:




