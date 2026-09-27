"""
Module 2 — Lesson 3: Loops & Lists
Student: [your name]
Date: [date]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[write your own explanation here]

A list is just like a collections of items, like a grocery list.
You can store multiple items in a list, and you can access them by their number.
But remember, the first item is always strarts 0, not 1.

A loop is a way to repeat a code block based on its condition. Theres different type of 
loops, one of this type is for loop, its very useful in list, specially when going through 
each items. While, a while loop repeats your code block under it, as long as the condition
is true.


============================================
KEY VOCABULARY
============================================
- list: collection of multiple items stored in a container or a variable.

- for loop: repeats the code block in a sequence or items in list. 

- while loop: repeats the code as long as the condition is true.

- index: Its like the location or number of the item in a list. It always 
starts with 0.

- iteration: One complete cycle of a loop.
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---

pets = ["Gagambino", "Zuma","Pulgoso"]

for pet in pets:
    print ("Wazzup", pet)

print (pets[1]) 

## Notice that it printed Zuma, not Gagambino. Because just like written in
## index, the numbering starts at 0

print (pets[0])

## See xD

print ("======================================")

print ("======================================")

num = 1;

while num <= 10:
    print (num)
    num = num + 1

## Its bacially reperating until i met a certain condition.


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]

One of the mistake I made and its confusing when im first year college is 
the while loop is running too much like i panicked a bit that time. Now i know that
don't leave while loop without stopping condition, because it can over run the cpu, 
resulting into freeze.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
