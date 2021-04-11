#!/usr/bin/env python
# coding: utf-8

# Here you have a collection of guided exercises for the first class on Python. <br>
# The exercises are divided by topic, following the topics reviewed during the theory session, and for each topic you have some mandatory exercises, and other optional exercises, which you are invited to do if you still have time after the mandatory exercises. <br>
# 
# Remember that you have 5 hours to solve these exercises, after which we will review the most interesting exercises together. If you don't finish all the exercises, you can work on them tonightor tomorrow. 
# 
# At the end of the class, we will upload the code with the solutions of the exercises so that you can review them again if needed. If you still have not finished some exercises, try to do them first by yourself, before taking a look at the solutions: you are doing these exercises for yourself, so it is always the best to do them your way first, as it is the fastest way to learn!

# **Exercise 1.1:** The cover price of a book is 24.95 EUR, but bookstores get a 40 percent discount. Shipping costs 3 EUR for the first copy and 75 cents for each additional copy. **Calculate the total wholesale costs for 60 copies**. 

# In[ ]:


#Your Code Here
Total_books = 60
price_per_book = 24.95
total_cost = price_per_book * 60

discount = total_cost * 0.4

Shipping_cost = 3 + (Total_books - 1) * 0.75

cost_of_60_books = total_cost-discount+Shipping_cost
print("total wholesale costs for 60 copies", cost_of_60_books)


# **Exercise 1.2:** When something is wrong with your code, Python will raise errors. Often these will be "syntax errors" that signal that something is wrong with the form of your code (e.g., the code in the previous exercise raised a `SyntaxError`). There are also "runtime errors", which signal that your code was in itself formally correct, but that something went wrong during the code's execution. A good example is the `ZeroDivisionError`, which indicates that you tried to divide a number by zero (which, as you may know, is not allowed). Try to make Python **raise such a `ZeroDivisionError`.**

# In[ ]:


#Your Code Here
2/0


# **Exercise 5.1**: Create a countdown function that starts at a certain count, and counts down to zero. Instead of zero, print "Blast off!". Use a `for` loop. 
# 

# In[ ]:


def countdown():

    number = 20

    while number != 0:
        print(number)
        number -= 1

    if number == 0:
        print("Blast off!")
    return
countdown()


# **Exercise 5.2:** Write and test three functions that return the largest, the smallest, and the number of dividables by 3 in a given collection of numbers. Use the algorithm described earlier in the Part 5 lecture :)

# In[ ]:


a = [2, 4, 6, 12, 15, 99, 100]
def largest(a):
    print("Largest number: " + str(max(a)))
    return max(a)

def smallest(a):
    print("Largest number: " + str(min(a)))
    return min(a)

def div_by_3(a):
    print("List of numbers divisable by 3:")
    for numbers in a:
        if numbers%3 == 0:
            print(numbers)
        else:
            pass
    return (numbers)

def main():
    largest(a)
    smallest(a)
    div_by_3(a)
    
    return (a)

main()

