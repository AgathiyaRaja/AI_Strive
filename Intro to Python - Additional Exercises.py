#!/usr/bin/env python
# coding: utf-8

# **Exercise 2.2 (optional):** Write code that classifies a given amount of money (which you store in a variable `amount`), specified in cents, as greater monetary units. Your code lists the monetary equivalent in dollars (100 ct), quarters (25 ct), dimes (10 ct), nickels (5 ct), and pennies (1 ct). Your program should report the maximum number of dollars that fit in the amount, then the maximum number of quarters that fit in the remainder after you subtract the dollars, then the maximum number of dimes that fit in the remainder after you subtract the dollars and quarters, and so on for nickels and pennies. The result is that you express the amount as the minimum number of coins needed.  
# 
# **Can you do it again? Would you change anything from the last time you had to do this?**

# In[ ]:


# Your Code Here


# **Exercise (optional)**: The factorial of a positive integer is that integer, multiplied by all positive integers that are lower (excluding zero). You write the factorial as the number with an exclamation mark after it. E.g., the factorial of 5 is `5! = 5 * 4 * 3 * 2 * 1 = 120`. Write a function that calculates the factorial of its (integer) parameter. Test your function for different parameter values, but do not use very large numbers as factorials grow exponentially. Hint: to do this with a `while` loop, you need at least one more variable.

# In[ ]:


# Factorial
def factorial(number):                                

    #Your Code Here

print(factorial(5))


# **Exercise 5.1 (optional):** Write a function that prints a multiplication table for digits 1 to 10. A multiplication table for the numbers 1 to `num = 3` looks as follows:
# 
# `. |  1  2  3`<br>
# `------------`<br>
# `1 |  1  2  3`<br>
# `2 |  2  4  6`<br>
# `3 |  3  6  9`
# 
# So the labels on the rows are multiplied by the labels on the columns, and the result is shown in the cell that is on that row/column combination. 

# In[ ]:


# Print multiplication table
def print_multiplication_table(n):
    
    #Your Code Here
        
print_multiplication_table(3)


# **Exercise 5.2 (optional):** If you did the previous exercise with a `while` loop, then do it again with a `for` loop. If you did it with a `for` loop, then do it again with a `while` loop. If you did not use a loop at all, you should be ashamed of yourself.

# In[ ]:


# Print multiplication table
def print_multiplication_table(n):
    
    #Your Code Here

print_multiplication_table(5)


# **Exercise 6.5 (optional):** Typical autocorrect functions are the following: 
# 1. if a word starts with two capitals, followed by a lower-case letter, the second capital is made lower case; 
# 2. if a sentence contains a word that is immediately followed by the same word, the second occurrence is removed; 
# 3. if a sentence starts with a lower-case letter, that letter is turned into a capital; 
# 4. if a word consists entirely of capitals, except for the first letter which is lower case, then the case of the letters in the word is reversed; and 
# 5. if the sentence contains the name of a day (in English) which does not start with a capital, the first letter is turned into a capital. 
# 
# Write a program that takes a sentence and makes these auto-corrections.

# In[2]:


# Autocorrect.
sentence = "as it turned out our chance meeting with REverend aRTHUR BElling was was to change our whole way of life, and every sunday we'd hurry along to St lOONY up the Cream BUn and Jam."


# ### Exercise 11.3 (Optional)
# In this directory you find a file `blakepoems.txt`. Write a program that processes the contents of this file, line by line. It creates an output file in the current working directory called `blkpms.txt`, which has the same contents as `blakepoems.txt`, except that all the vowels are removed (case-insensitively). At the end, display how many characters you read, and how many characters you wrote. If you want to check the contents of `blkpms.txt`, you can either open it in a text editor, or display the first 10 lines or so at the end of your program.

# In[ ]:


## Your Code Here

