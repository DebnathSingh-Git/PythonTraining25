# Assignment 1: List All .txt Files and Check for a Word using glob + re.search
# Write a script to:
# - Find all .txt files in a folder.
# - Check if any file contains the word "Python".
# - Print the file name if the word is found

import glob
import re
import os

print("Assignment 1")
files = glob.glob("D:\\Linux-Dev\\PYHTON\\Python_Training\\glb\\*")
# print(files)

for f in files:
    res = re.search(r"new Python",f)
    if res:
        print(f"Found the pattern {res.group()} in {f}")


print("-" *50)
print("Assignment 2")
# Assignment 2: Match File Names Using re.match
# List all files in a folder using glob, and print only the ones that start with "data_" and end with ".csv".
        
files = glob.glob("D:\\Linux-Dev\\PYHTON\\Python_Training\\glb\\*")
# print(files)

for f in files:
    # print(f)
    filename = os.path.basename(f)
    res = re.match(r"^data_.*\.csv$", filename)
    if res:
        print(f"Found the pattern {res.group()} in {f}")    


print("-" *50)
print("Assignment 3")
# Assignment 3: Validate Phone Numbers with re.match
# Given a list of phone numbers, print only the ones that match this format:
# (123) 456-7890

phonenolist = ["033 2675990", "(123) 456-7890", "(999) 9999999", "011 345-6789", "(999) 689-7007", "(999) 123-45678"]

for ph in phonenolist:
    res = re.match(r"^\(...\) ...-....$", ph.strip())
    if res:
        print(f"Found phone {res.group()}")  