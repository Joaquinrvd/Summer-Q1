#1. create an empty dictionary 
#2. prompt the user for the student name key
#3. prompt the user for the student age key
#4. prompt the user for the student grade key
#5. prompt the user for the student hobbies key (a nested list)
#6. print the dictionary to the consle

student = {}

studentName = input("Enter your Student's name: ")
student["Name"] = studentName

print(student)

studentAge = input("Enter Your Student's age: ")
student["Age"] = studentAge

print(student)

studentGrade = input("Enter Your Student's grade: ")
student["Grade"] = studentGrade

print(student)

Hobbies= []

studentHobbie =input("enter hobbies enter done when done")
Hobbies.append(studentHobbie)

while studentHobbie != "done":
    studentHobbie =input("enter hobbies enter done when done")
    Hobbies.append(studentHobbie)
student["Hobbies"] = Hobbies

print(student)