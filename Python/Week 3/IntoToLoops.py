geniuses = ["Tay", "Kristopher", "Kamari", "Jeffrey"]

for genius in geniuses:
    print(genius)

answer = input("Woukd you like me to print this again Y/N? ")
while answer == "Yes":
    for genius in geniuses:
        print(genius)
    answer = input("Woukd you like me to print this again Y/N? ")

while answer == "yes":
    for genius in geniuses:
        print(genius)
    answer = input("Woukd you like me to print this again Y/N? ")

while answer == "no":
    answer = input("Ok, enjoy your day Y/N. ")

while answer == "No":
    answer = input("Ok, enjoy your day Y/N. ")