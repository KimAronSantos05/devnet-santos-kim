"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: [your name]
Date: [date]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[write your own explanation here]

Basically, its how your code flows based on a given condition.
It can be in a way of if/elif/else statements. For example, a program can 
check whether a student has passed or failed the course based on their grade
and given a certain condition. If the grade is above 75, then the student has 
passed, or if (elif) the grade is below 75, then the student has failed. Another
way is to apply operators, which can be use to compare values. For example,
if the grade is grated than of equal to 75 print "You passed", basically it
will check if the grade is greater than or equal to 75, then it will 
print "You passed". So yeah, thats how your code can flow based on a given condition. 


============================================
KEY VOCABULARY
============================================
- condition: Its something that your program check where to flow or decide.

- if / elif / else: 
    -if: It first check this condition, if its true, then it will execute
    the code under this condition.
    -elif: When if is not met, then your code will now check this condition,
    when it met this condition, then the code under this will be executed.
    -else: If none of the above conditions are met, then the code under 
    this will be executed.

- comparison operator: This are operators like =, <, >, !. They are used to compare values

- boolean expression: A expression that checks if the condition is true or false.
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---
print("=====Grade Checker=====")
grade = int(input("Enter your grade: "))

if grade >= 90:
    print("You aced the course!")
elif grade >= 75:
    print("You clutched the course!")
else:
    print("GGS, better luck next time!")



"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]

The mistake and confusing part for me before is the flow of the condtion itself in if,
elif, and else. When you first write the lowest possible condition in if, the elif and
else will not be executed because the first conditiion or the if is already met.
So basically, the order of the conditions is also important. You have to write the highest
condition first, then the lowest condition last.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]

In life, when we make a decision, we can have different outcomes based on the 
condition or choices we make. Its not linear, you are just like the program, and 
the world will give you some conditions. Whatever you choose, there your life will flow.
"""
