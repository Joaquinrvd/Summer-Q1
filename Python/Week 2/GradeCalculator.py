numberGrade = int(input("Enter number grade from 1-100: "))
letterGrade =""

if (numberGrade >= 90):
    letterGrade = "A"
elif (80 <= numberGrade <= 89):
    letterGrade = "B"
elif (70 <= numberGrade <= 79):
    letterGrade = "C"
elif (60 <=numberGrade <= 69):
    letterGrade = "D"
elif (numberGrade <=60):
    letterGrade = "F"



print("You have a " + letterGrade)
