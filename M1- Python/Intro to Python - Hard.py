#!/usr/bin/env python
# coding: utf-8

# Here you have a collection of guided exercises for the first class on Python. <br>
# The exercises are divided by topic, following the topics reviewed during the theory session, and for each topic you have some mandatory exercises, and other optional exercises, which you are invited to do if you still have time after the mandatory exercises. <br>
# 
# Remember that you have 5 hours to solve these exercises, after which we will review the most interesting exercises together. If you don't finish all the exercises, you can work on them tonightor tomorrow. 
# 
# At the end of the class, we will upload the code with the solutions of the exercises so that you can review them again if needed. If you still have not finished some exercises, try to do them first by yourself, before taking a look at the solutions: you are doing these exercises for yourself, so it is always the best to do them your way first, as it is the fastest way to learn!

# **Exercise 4.1 (🌶️🌶️):** Define a function that receives a string parameter, and returns an integer indicating the count for all the letters of the alphabet that there are in the string. The expected output format is in a **dictionary** with the relevant keys and values. The capital version of a lower case letter is considered to be the same letter.
# 
# This should sound quite familiar, try to do it without looking at your old code ;)
# 
# **What is the challenge?**: Don't code 27 times the same line of code, learn how to do things that scale well.

# In[1]:


#Your Code Here
def alphabet_check(word):

    alphabet = {}
    clean_word = word.lower()

    for letter in clean_word:
        print(letter)
        if letter in alphabet.keys():
            alphabet[letter] += 1
            if alphabet[letter] == 1:
                pass
        else:
            alphabet[letter] = 1

    print(alphabet.values())
    return

alphabet_check("Hello")


# **Exercise 5.6 (🌶️🌶️):** A prime number is a positive integer that is dividable by exactly two different numbers, namely 1 and itself. The lowest (and only even) prime number is 2. The first 10 prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23, and 29. Write a function that returns a **list off all prime numbers** below a given number.
# 
# Hint: In a loop where you test the possible dividers of the number, you can conclude that the number is not prime as soon as you encounter a number other than 1 or the number itself that divides it. However, you can *only* conclude that it actually *is* prime after you have tested all possible dividers.
# 
# **What is the challenge here? You have to try to optimize your code and try to make it work for the highest prime number you can encounter before you run out of memory. For low numbers you should know how to do it already**

# In[2]:


#Your Code Here
def prime_numbers(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

prime_numbers(10)


# **Exercise 5.7 (🌶️🌶️):** Write a function that prints all integers between the parameters `a` and `b` that can be written as the sum of two squares. Produce output in the form of `z = x**2 + y**2`, e.g., `58 = 3**2 + 7**2`. If a number occurs on the list with multiple *different* ways of writing it as the sum of two squares, that is acceptable. 

# In[3]:


#We struggled to understand the logic even with the solution present, but we now understand
#All that matters is the final number (z)
#you create a clear range that the whole program runs on, so all variables are working in the same range (including z)
#the only relevant output is when numbers in the given range squared and added = z
#we cleaned up the int to str on line 12 by using commas instead of type conversions and +
def sum_squares(a,b):
    for z in range(a,b):
        for x in range(b):
            for y in range(b):
                if x**2 + y**2 == z:
                    print(z,"=",x,"**2 + ",y,"**2")

    """
    2 = 1**2 + 1**2  the numbers 0^2= 0, 1^2=1, 2^2=4, 3^2= 9  
    4 = 0**2 + 2**2
    4 = 2**2 + 0**2
    5 = 1**2 + 2**2
    5 = 2**2 + 1**2
    8 = 2**2 + 2**2
    9 = 0**2 + 3**2
    9 = 3**2 + 0**2
    """
    return

sum_squares(1,10)


# In[ ]:




