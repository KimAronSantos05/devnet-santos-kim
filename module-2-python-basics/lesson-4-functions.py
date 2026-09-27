"""
Module 2 — Lesson 4: Functions
Student: Santos, Kim Aron C.
Date: 09-27-26

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[write your own explanation here]

A function is a block of reusable codes that performs a specific task. Instead of re-typing
the code lines that do the same thing in your project. You can just make a function and call
it whenever u will do a repetitve command.

============================================
KEY VOCABULARY
============================================
- functions: A block of reusable code that performs a specific task.
- def: the keyword for creating a function.
- parameter: it served as a placeholder for incoming info which is the arguement. It was placed
also in parentheses but in the defined function above.
- arguments: this are information that can be passed into function. These are placed
inside the parentheses when the function is called below.

============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---

print ("== FAMILY SANTOS ==")

def name(fname):
    print(fname, "Santos")

name("Marlon")
name("Bernadette")
name("Kim Aron")
name("Kimberly")
name("Trisha Mae")
name("Trisha Lyn")

print ("==== ==== ==== ====")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]

There is actually a confusion between parameter and arguments. A parameter is a variable
written inside the def function parentheses. While, arguments are is written in the 
parentheses when the function is called. 

def name(fname):                 <--- This is the parameter
    print(fname, "Santos")

name("Marlon")                   <--- This is the argument

Note: Remember also that the parameter is unique and different from the function name
      because it only acts as the placeholder that when a argument is set, it will be
      passed in parameter. 

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]

We can connect it in a quote saying "Work Smarter, not Harder". Because, instead of 
manually typing all the code that just repeats on your work, why not just use function
so that you will just write a single line of code whenever u want to execute it.
In that way you can save effort and time.

"""
