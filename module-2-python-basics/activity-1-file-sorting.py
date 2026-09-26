"""
Module 2 — Activity: File Sorting with os and shutil
Student: [your name]
Date: [date]

============================================
WHAT DID YOU BUILD? (explain in your own words)

============================================
[Paste your working script below first, then come back and explain
it here: what does your script do, and what rule did you use to
sort the files? e.g. by extension, by name, by date, etc.]


============================================
KEY VOCABULARY
============================================
- os module: built-in python modules that provides
pre-built system function that doesn't need to be coded
in your own project.

- shutil module: a type of os module that checks file
paths inside your computer.

- file path: Its the exact location of a file or
a folder inside the computer.

- directory: I think its also a folder that contains
files. Its just a different name for it.
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

storage = input ("Type a folder path: ")

if os.path.exists(storage):
  print("Moving....")
  print ("All folders & files:", os.listdir())
else:
    print ("No such folder path. ngekkk")

os.mkdir("Image")
os.mkdir("Documents")
os.mkdir("Videos")
os.mkdir("Others")

# --- paste your existing code here ---


"""
============================================
A MISTAKE I MADE (or one I want to avoid)

I tried my best to build a script that sorts files into folders
based on their file types. But the problem is, i only created a path checker
if the path exists, and also i used mkdir to only create files but didn't work
as i planned.

============================================
[what tripped you up while building this? e.g. a path that didn't
exist, a file that got overwritten, something that didn't work the
way you expected at first]

I think its the mkdir that didn't work as i planned,
because its just created a folder and create again, 
like its just works as directory creator. xD

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]

"""
