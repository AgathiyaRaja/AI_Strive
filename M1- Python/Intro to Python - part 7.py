#!/usr/bin/env python
# coding: utf-8

# # Chapter 11 - Text Files

# ---

# One of the most important uses of Python for data processing is the reading, changing, and writing of text files. Data is often stored in text files, because text files can be easily transferred between different programs. There are multiple standardized formats for text files, such as "comma-separated values" (CSV) files. Python supports particular text file formats through modules, some of which will be discussed later. This chapter focusses on opening, reading, writing, and closing of any text file, regardless of format. 

# ---

# ## Flat text files

# When programmers refer to "text files" or "flat text files", they mean files in which all characters are meant to be read as regular characters, like you would type on a keyboard. For instance, Python program files are flat text files, as are HTML files. Word processor documents, however, are not flat text files, and neither are images. If you want to know whether a file is a text file or not, you can try to open it in a text editor (such as the editor for the IDLE environment, which comes with Python). If you see only readable text, the file is likely to be a text file. Otherwise, it is a so-called "binary file".
# 
# Text files consist of lines of text. At the end of a line, there is a "newline" symbol, which in Python is the character "`\n`". Different operating systems use slightly different ways of storing this character in a text file: some Windows programs store it as "carriage return", as well as "line feed" ("`\r\n`", sometimes thought as a leftover from old typewriters), while on Linux it is always stored as a single "`\n`". As long as you access a file from Python as a regular text file, Python will convert the characters that it reads to the standard "`\n`", and vice versa when it writes. So you do not usually need to worry about such differences (except when you need to transfer text files between operating systems).
# 
# However; if you open a file in other editors, such as notepad, sometimes it does not properly understand the end-of-line characters, and shows everything on one line.

# ### File handles and pointers

# When you work with a file in a program, you have to open the file. Opening a file provides a so-called "file handle". A file handle can be seen as an access point to the file. It contains a "pointer" that indicates a particular place in the file. That pointer is used when you read from or write to the file. For instance, when you read from the file, it starts reading at the pointer, and moves the pointer forward in the file.
# 
# When you open a file, the pointer is placed at a particular spot in the file, depending on how you opened the file. If you opened the file for reading only, the pointer is placed at the start of the file. The same is true when you open the file for both reading and writing. If you open the file for "appending" (i.e., to place new data at the file's end), the file pointer is positioned at the end of the file. Lastly, if you open a file for writing only, actually the file is completely emptied and the file pointer is placed at the start of the, now empty, file. To create a new file (i.e., a file with a name that does not exist yet), you open it for "writing only".
# 
# After opening the file, the file handle is the only access point for the file. All actions you perform on the file, you perform as methods for the file handle.
# 
# Note that any operating system only allows a limited number of files to be open simultaneously. Therefore you should close files that you no longer need to work with.

# ### Moving the file pointer

# The file pointer, that indicates where in a file you are working, is moved automatically. For instance, when you read 10 characters from a file, the file pointer indicates which is the first of those 10 characters, and, while reading, moves up 10 characters, so that its new position is 10 characters further in the file than before. When you deal with text files, the automatic movements of the file pointer are exactly what you want. You *can* position the file pointer manually using specific methods, but such methods are, in general, only used when dealing with binary files. 

# ### Buffering

# When you make changes to files, these often are not stored in the files immediately. Instead, the operating system "buffers" the changes in memory, and "flushes" the buffers to the actual files when it sees a need for that. You can force the flushing of the buffers by closing a file. Buffers are also flushed when your program ends normally.
# 
# However, when your program crashes (for instance because of a runtime error), buffers might not be flushed, and your files will not be updated to the point where the crash took place. So you cannot take the file contents into account when trying to debug a program.

# ### File processing programs

# Most programs that deal with text files follow a process that, in a loop, reads contents of a file, processes those contents in some way, then writes the contents to another file. For instance, a program might read lines from a text file, and for each line sort the words, then write the sorted words to another text file. This is hardly any different from a program that asks the user the provide, in a loop, a line of text, then sorts the words in the line, and displays them using the `print()` function. 
# 
# However, it tends to be experienced as more complicated.
# 
# When you provide input to a program manually, and see it displaying outputs, you always know more or less what lines of your code Python is processing, and you can make up tests on the fly. If you work with files, you have to prepare your files beforehand, then run the program and wait until it finishes before you can examine the contents of the output files. 
# 
# While working with files might give a sense of lack of control, during development of the program you can always include `print()` statements to get an insight in what the program is doing. For instance, when it reads a line, you can print that line, and when it writes a line, you can also print that line. That way, your insight in the inner workings of the program is no different regardless whether you use manual inputs and screen outputs, or file inputs and outputs.

# ---

# ## Reading text files

# To read the contents of a file, you must first open it, then read the contents, then close it.

# ### Opening a file using `open()`

# To open a file, you use the `open()` function. 
# 
# The `open()` function gets two arguments, of which the second one is optional. The first argument is the name of the file. If the file is not in the current directory, you have to include the complete path to the file so that Python can find it. The second argument is the "mode". The mode indicates how you want to treat the file. The default mode (which is picked when you do not supply the second argument) is opening the file as a text file for reading only. How you set other modes is discussed later.
# 
# The `open()` function returns a file handle, which you use for all the remaining functionalities.
# 
# Rather than writing "`<handle> = open( <filename> )`", you will often see Python programs that write this as "`open( <filename> ) as <handle>`". These two ways of writing code are equivalent. I myself prefer the first, as that is the way it is done in most programming languages. However, the second method has an advantage that I discuss below, when talking about closing a file.

# ### Reading a file using `read()`

# The simplest way to read the contents of a file is using the `read()` method, without arguments, on the file handle. This returns a string that contains the complete contents of the file. `read()` can get an argument, but that's only used for binary files.
# 
# Reading from a file moves the file pointer to right after the part of the file that was read. This means that if you use the `read()` method without arguments, the file pointer is moved to the end of the file. This entails that if you would try to `read()` from it a second time, nothing would be read, as there is nothing to be read after the spot where the file pointer is.

# ### Closing a file using `close()`

# To close a file, you use the `close()` method on the file handle. Every file that you open, you should close at some point in your program. This is especially true in these notebooks, as each notebook page is considered to be one complete program; this means that if you do not close a file, it remains open even after the bit of code that you executed ends.
# 
# If everything that you need to do with a file is done in a single block, you can write this block as follows:
# 
#     with open( <filename> ) as <handle>:
#         <statements>
#         
# This syntactic construction has the advantage that the file will be closed automatically after the block `<statements>` ends, so you do not need to include an explicit `close()` call. This construction is typically Python; you do not see it in many other programming languages.

# ### Displaying the contents of a file

# Now the first few functions and methods for dealing with text files have been introduced, I can show some code that reads the contents of a file.

# In[1]:



def display_contents_file(file_name):
    #fp = open(file_name, "r")
    with open( file_name ) as fp:
        buffer = fp.read()
    print( buffer )
    
display_contents_file("Shakespeare.txt")


# In[3]:



def display_contents_file(file_name):
    fp = open(file_name, "r")
    #with open( file_name ) as fp:
    buffer = fp.read()
    print( buffer )
    fp.close()
display_contents_file("Shakespeare.txt")


# In[4]:


def display_contents_file(file_name):
    #with open( file_name ) as fp:
    fp = open(file_name, "r")
    buffer = fp.readlines()
    for line in buffer:
        print(line)
    print(buffer)
    fp.close()
    
display_contents_file("Shakespeare.txt")


# ### Reading lines using `readline()`

# To read a text file line by line, you can use the `readline()` method. The `readline()` method reads characters starting at the file pointer up to and including the next newline character, and returns them as a string. You can recognize that you have reached the end of the file by the fact that no characters are read anymore, i.e., the string that is returned is empty.

# In[5]:


def display_contents_file2(file_name):
    fp = open( file_name , "r")
    buffer = fp.readlines()
    print(buffer)
   # for line in buffer:
    #    print (line)
    #fp.close()
    
display_contents_file2("Shakespeare.txt")


# In[6]:


def display_contents_file2(file_name):
    fp = open( file_name )
    while True:
        buffer = fp.readline()             
        if buffer == "":
            break     
        print( buffer )
    fp.close()
display_contents_file2("Shakespeare.txt")


# In[7]:


fp = open("Shakespeare.txt", "r")                                       
list_ = fp.readline()
print (list_)
#for line in line:
 #   print(line)

#print(fp.readline())
fp.close ()


# Notice that the output of the code above has an empty line between each of the lines displayed. Where is that extra line coming from? Think about it.
# 
# The extra line is there because the `readline()` method returns a string of the characters read, up to and *including* the newline character. So when the `buffer` is printed, it prints a newline character too. And since the `print()` function *also* moves to a new line after it is executed, there is an empty line printed after each line of text.

# A collary to the `readline()` method is the `readlines()` method. `readlines()` reads all the lines in the file, and returns them as a list of strings. The strings include the newline characters.

# ### When to use which file-reading method

# Both the `read()` and `readlines()` method read a whole file at once. Obviously, for small files this is acceptable, but for long files you might not have enough memory to store the file contents efficiently. In such circumstances (or when you do not know the file size), you should read a file line by line with the `readline()` method.
# 
# It is often a good idea, during code development, to process only the first few lines of a file. That way you limit the amount of time that the program needs to process a file, and limit its output, which makes debugging easier. For instance, the code below process the first 10 lines of one of the longer files.

# In[10]:


def display_contents_file4(file_name):
    fp = open(file_name)
    count = 0
    while count < 10:
        buffer = fp.readline()
        if buffer == "":
            break
        print( buffer, end="" )
        count += 1
    fp.close()
    
display_contents_file4( "Shakespeare.txt")


# Once the program is finished and debugged, I can remove the references to `count` and change the loop to `while True`, to process the whole file.
# 
# **Exercise**: Start by copying the code above in the code block below. Then adapt it to count how often the word "from" (with any capitalization) occurs in the text as a whole. Print only the number of occurrences of that word. If you do it correctly, you find the answer is 14 (it occurs 3 times in the first 20 lines).

# In[11]:


def display_contents_file4(file_name):
    #Your Code Here
    
display_contents_file4( "Shakespeare.txt")


# 

# ## `os.path` methods

# At this point you know everything you need to handle text files in Python. However, there are several handy functions that make your life easier when dealing with files. These are collected in the `os.path` module. As per usual, I am not going to list all of them, but I will list the ones that you will use the most.
# 
# In these functions, the term "path" refers to a filename or a directory name, complete with parent directories (and drive letter). The parent directories (and drive letter) do not *need* to be there explicitly, but even if they are not, implicitly they still are as each file and each directory is located in a particular place in the file system.

# ### `exists()`

# The function `exists()` gets a path as argument, and returns `True` if that path exists, and `False` if it does not.

# In[21]:


from os.path import exists

def check_if_path_exists(file_name):
    if exists(file_name ):
        return( file_name + " exists" )
    else:
        return( file_name + " does not exist" )

print(check_if_path_exists("Shakespeare.txt"))
print(check_if_path_exists("TorresMapfre.txt"))

exists("Shakespeare.txt")


# ### `isfile()`

# `isfile()` tests if the path that is supplied as argument is a file. If it is, it returns `True`. If it is not, it returns `False`. If the path does not exist, the function also returns `False`.

# In[22]:


from os.path import isfile

def check_if_file_exists(file_name):
    if isfile( file_name ):
        return( file_name + " is a file" )
    else:
        return( file_name + " is not a file" )
    
print(check_if_file_exists("Shakespeare.txt"))


# ### `isdir()`

# `isdir()` tests if the path that is supplied as argument is a directory. If it is, it returns `True`. If it is not, it returns `False`. If the path does not exist, the function also returns `False`.

# In[24]:


from os.path import isdir

def check_if_path_is_dir(file_name):
    if isdir( file_name):
        print( file_name + " Sheakspeare is a directory" )
    else:
        print(file_name + " is not a directory" )
check_if_path_is_dir("Shakespeare.txt")


# ### `basename()`

# `basename()` extracts the filename from a path, and returns it. 

# In[27]:


from os.path import basename

print( basename( "/System/Home/readme.txt" ) )


# ### `dirname()`

# `dirname()` extracts the directory name from a path, and returns it.

# In[28]:


from os.path import dirname

print( dirname( "/System/Home/readme.txt" ) )


# ### `getsize()`

# `getsize()` gets the size of the file that is supplied as argument, and returns it as an integer. The file must exist, otherwise you get a runtime error.

# In[30]:


from os.path import getsize

numbytes = getsize( "Shakespeare.txt" )
print( numbytes )


# ---

# ## File encoding

# Text files use an "encoding", i.e., a system that prescribes how characters in the files are supposed to be interpreted. This encoding may differ between operating systems. You can see the preferred encoding that your system uses with a call to `sys.getfilesystemencoding()`.

# In[48]:


from sys import getfilesystemencoding

print( getfilesystemencoding() )


# If you read a text file which uses a different encoding than your file system prefers, you may get a `UnicodeDecodeError`. Whether or not you get this error for a particular file, is related to your operating system. An annoying consequence of that is that when you port Python code that reads a file to another system, a file that could be read by your code previously may cause your code to crash after the port.
# 
# An easy way to get around this problem is by adding an extra parameter when opening a file, which indicates the encoding mechanism that you want to use when reading the file. You do this by adding a parameter "`encoding=<encodingname>`", where `<encodingname>` is a string that can have a variety of values, for which some typical ones are:
# 
#     ascii       7-bits encoding, supports characters with values in the range 00-7F
#     latin-1     8-bits encoding, supports characters with values in the range 00-FF
#     mbcs        2-byte encoding, that is currently getting replaced by UTF-8
#     utf-8       variable bytes encoding
# 
# Typically, text files are created with `ascii` or `latin-1` encoding. Since `ascii` is incorporated in `latin-1`, you can safely open any text file by specifying `latin-1` as encoding. It is possible that for the characters beyond the `ascii` range, you get different characters than the person who created the file wanted you to see -- that depends on the encoding mechanism that your file system uses. But at least the `UnicodeDecodeError` is avoided.
# 
# Note that while `utf-8` supports a much wider range of characters than `latin-1`, you may still get the `UnicodeDecodeError` when you read a text file that uses `latin-1` encoding on a system that uses `utf-8` encoding, as `utf-8` has no corresponding characters with values in the range 80-FF.
# 

# **Exercise**: If you change the encoding mechanism for this file to `utf-8`, it will enforce the `UnicodeDecodeError` as it contains characters with numbers in the range 80-FF. Try this.
# 
# If you want to see which special characters are supported with values in the range 80-FF on your system, run the code below. The numerical value of a character in the table can be derived by calculating `16*row+col`, whereby `row` and `col` are the hexadecimal row and column number, respectively. I do not display the characters in the range 80-9F, as these are normally not filled in.

# In[31]:


#Your Code Here


# ---

# ## What you learned

# In this chapter, you learned about:
# 
# - Text files
# - File pointers
# - Opening and closing files with `open()` and `close()`
# - Reading files with `read()`, `readline()`, and `readlines()`
# - Writing files with `write()` and `writelines()`
# - Appending to files
# - `os.path` methods `exists()`, `isfile()`, `isdir()`, `join()`, `basename()`, `dirname()`, and `getsize()`
# - Dealing with text files with different encoding mechanisms

# ---

# ## Exercises

# ### Exercise 11.1

# Write a program that reads the contents of the file "`blakepoems.txt`", splits it into words (where everything that is not a letter is considered a word boundary), and case-insensitively builds a dictionary that stores for every word how often it occurs in the text. Then print all the words with their quantities in alphabetical order.

# In[18]:


# Counting words in blakepoems.txt.
import os
path = os.getcwd()
print(path)

"""
path3 = "D:\Strive_school\ai_mar21\M1_Python\d4_Strings_and_files"
path = os.chdir( path2 )
print(path)

"""
fp = open( "D:\Strive_school\ai_mar21\M1_Python\d4_Strings_and_files\text-files\blakepoems.txt")
buffer = fp.read()
print( buffer )

    


# ### Exercise 11.2

# Do the same thing as you did for the previous exercise, but now process the text line by line. This is something that you would have to do if you had to process a very long text (as it is the case).

# In[ ]:


# Counting words line by line.
def count_words(file_name):
    dic = dict()
    fp = open(file_name, "r")
    buffer = fp.readlines()
    for line in buffer:
        line = line.strip().lower()
        words = line.split(" ")
        for i in words:
            if i in dic:
                dic[i] = dic[i] + 1
            else:
                dic[i] = 1

    fp.close()
    return dic


print(count_words("text-files/blakepoems.txt"))


# ---
