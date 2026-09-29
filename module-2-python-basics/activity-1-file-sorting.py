"""
Module 2 — Activity: File Sorting with os and shutil
Student: [Dhayle Tabamo]
Date: [September 27, 2026]

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[It is a File Sorting program as the name suggest it sorts file by category
how it does this is first it ask for the path of the directory you want to sort,
of course it has to check the directory exist it then create a sub folder where it can
put each files into so they could be sorted, after that it loops trough the directory
skipping the subfolders and moving the files e.g. the ones that ends with .jpg, .jpeg, .png, .gif
goes to images folder, .pdf, .docx, .txt, .pptx goes to documents folder, .mp4, .mov, .avi goes to
the videos folder, and everything else goes to others folder. For every files moved the counter 
for each folder increments to 1 for the summary after the program
finished sorting(there are some mistakes prbably when running, sometimes it runs too long in vs code or can't find the path)]


============================================
KEY VOCABULARY
============================================
- os module: This is what the python uses to basically interact with the operating system, it can be used after importing it using import os command.
- shutil module: This module shutil/ sh util/ shell utilities is used to grant the program  a higher function like letting it interact with files like moving them.
- file path: It is the path that a file or folder was in for example C:\Users\Dhayle\GamedevProject
- directory: A folder, that's how would i explain it, a folder that can contain files or other folders(directories).
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

p = input("Enter the folder path to organize: ")

if os.path.exists(p) == True:

    fileList = os.listdir(p)

    imgCount = 0
    docCount=0
    vidcount = 0
    othr_count = 0

    for f in fileList:
        if f=="Images" or f == "Documents" or f=="Videos" or f == "Others":
            continue


        if os.path.isdir(fullpath)==True:
            continue

else:
    print("that folder doesnt exist, try again")
# --- paste your existing code here ---


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[uuhh the first version can't find the directory so it will always print this directory doesn't exist
turns out there are unecessary characters and wrong spelling most of the time when putting the path 
i don't know if there is a lazy way to fix it like at least a code that can clear out special characters
so I don't need to tripple check every time I put a new path.]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
