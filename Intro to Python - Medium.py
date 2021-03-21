#!/usr/bin/env python
# coding: utf-8

# Here you have a collection of guided exercises for the first class on Python. <br>
# The exercises are divided by topic, following the topics reviewed during the theory session, and for each topic you have some mandatory exercises, and other optional exercises, which you are invited to do if you still have time after the mandatory exercises. <br>
# 
# Remember that you have 5 hours to solve these exercises, after which we will review the most interesting exercises together. If you don't finish all the exercises, you can work on them tonightor tomorrow. 
# 
# At the end of the class, we will upload the code with the solutions of the exercises so that you can review them again if needed. If you still have not finished some exercises, try to do them first by yourself, before taking a look at the solutions: you are doing these exercises for yourself, so it is always the best to do them your way first, as it is the fastest way to learn!

# **Exercise 1.3 (🌶️):** You look at the clock and see that it is currently 14.00h. You set an alarm to go off 535 hours later. At what time will the alarm go off? Write a program that prints the answer. Hint: for the best solution, you will need the modulo operator. Second hint: The answer is 21.00h, but of course, this exercise is not about the answer, but about how you get it.

# In[1]:


#Your Code Here
current_time = 14.00
alarm_after = 535
alarm_time = (14+535) % 24
print("The alarm goes off around", alarm_time)


# **Exercise 5.4 (🌶️):** "99 bottles of beer" is a traditional song in the United States and Canada. It is popular to sing on long trips, as it has a very repetitive format which is easy to memorize, and can take a long time to sing. The song's simple lyrics are as follows: "99 bottles of beer on the wall, 99 bottles of beer. Take one down, pass it around, 98 bottles of beer on the wall." The same verse is repeated, each time with one fewer bottle. The song is completed when the singer or singers reach zero. Write a function that generates and prints all the verses of the song (though you might start a bit lower, for instance with 10 bottles). Make sure that your loop is not endless, and that you use the proper inflection for the word "bottle".

# In[ ]:


def beersong():
    number = 10

    while number != 2:
        print(str(number) + " bottles of beer on the wall, " + str(number) + " bottles of beer. Take one down, pass it around, ", end='')
        number -= 1
        print(str(number) + " bottles of beer in the wall")

    if number == 2:
        print(str(number) + " bottles of beer on the wall, " + str(number) + " bottles of beer. Take one down, pass it around, ", end='')
        number -= 1
        print(str(number) + " bottle of beer in the wall")

    if number == 1:
        print(str(number) + " bottle of beer on the wall, " + str(number) + " bottle of beer. Take one down, pass it around, ", end='')
        number -= 1
        print(str(number) + " bottles of beer in the wall")
    return

beersong()


# **Exercise 5.5 (🌶️):** The Fibonacci sequence is a sequence of numbers that starts with 1, followed by 1 again. Every next number is the sum of the two previous numbers. I.e., the sequence starts with 1, 1, 2, 3, 5, 8, 13, 21,... Write a function that calculates and prints the Fibonacci sequence until the numbers get higher than a `maximum`.

# In[3]:


#Needs to be capped at 22
def fibonacci():

    count = 0

    num_a = 0
    num_b = 1
    num_c = 0

    while count <= 8:
        print(num_a)
        num_c = num_a + num_b
        num_a = num_b
        num_b = num_c
        count += 1
    return
fibonacci()


# **Exercise 5.8 (🌶️):** A, B, C, and D are all different digits. The number DCBA is equal to 4 times the number ABCD. What are the digits? Note: to make ABCD and DCBA conventional numbers, neither A nor D can be zero. Use a quadruple-nested loop.

# In[ ]:


def nested_nest():
    for a in range(1,10):
        for b in range(1,10):
            for c in range(1,10):
                for d in range(1,10):
                    if 4*((a*1000) + (b*100) + (c*10) + d) == (d*1000) + (c*100) + (b*10) + a:
                        return a, b, c, d
nested_nest()

