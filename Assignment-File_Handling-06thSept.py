# File Handling:
# A school wants to maintain student records using a text file. 
# You are required to write a Python program that performs the following file handling operations step by step:

# ----------------------------------------------------------------------
import os
# 1) Write Operation:
# - Create a file named students.txt.
# - Write details of students (Name, Roll Number, Marks) into the file.
def writeop():
    with open("students.txt", 'a') as f:
        name = input("Student Name: ")
        roll = int(input("Roll Number: "))
        markscience = int(input("Science Marks: "))
        markmaths = int(input("Maths Marks: "))
        f.write(f"{name}, {roll}, {markscience}, {markmaths}\n")
        f.close()
 
# 2) Read Operation:
# - Read the content of students.txt and display it on the screen.
def readop():
    with open("students.txt", 'r') as f:
        lines = f.readlines()
        for l in lines:
            print(l)
        f.close()

# 3) Rename Operation:
# - Rename the file from students.txt to student_records.txt.
def renameop():
    os.rename("students.txt", "student_records.txt")

 
# 4) Directory Operations:
# - Create a directory called SchoolData.
# - Move the renamed file student_records.txt into this directory.
# - List all files present in SchoolData to confirm the file is inside.
def directoryop():
    os.mkdir("SchoolData")
    os.replace("student_records.txt", os.path.join("SchoolData", "student_records.txt"))
    filefolderlist = os.listdir("SchoolData")
    for f in filefolderlist:
        print(f)
 
# 5) Delete Operation:
# - Delete the file student_records.txt from inside the directory. 
# Finally, delete the SchoolData directory.
def deleteop():
    os.remove(os.path.join("SchoolData", "student_records.txt"))
    os.rmdir("SchoolData")

 
# 6) Do create a menu taking the user input and then perform the operation
def menu():
    while True:
        print("\n======== Product Menu========")
        print("1. Write operation")
        print("2. Read operation")
        print("3. Rename operation")
        print("4. Directory operation")
        print("5. Delete operation")
        print("6. Exit")
       
        choice = input("Enter choice(1-6): ")
       
        if choice == "1":
            writeop()
           
        elif choice == "2":
            readop()
           
        elif choice == "3":
            renameop()
       
        elif choice =="4":
            directoryop() 
       
        elif choice =="5":
            deleteop()
       
        elif choice =="6":
            break
           
        else:
            print("Wrong option !!")
           
if __name__ == "__main__":
    menu()

    