# This program will allocate teams from a list of names
# 1. Import the random module
# 2. create a list of every Genius 
# 3. use the random module to randomly suffle the list
# 4. loop through the list and display each teams each teams players
# 5. Using an if statement to see if the user is happy  with the teams 
# If not, it will shuffle again. If so, the program terminates 



import random # Import the random module

#create a list of players stored in the player variable
players = ["Devon", "Kauri", "Isaiah",
            "Braylen", "Taymur", "Xavier",
            "Avery", "Taqari", "Kenlon",
            "Marshawn", "Nahum","Kamari",
            "Kristopher", "Joseph", "Darren", 
            "Carl", "Walter", "Jeffrey", 
            "Nishad", "Maximus", "Ja’Den", 
            "Jarmauri", "Eustace", "Semaj", "Joaquin"]

def PickTeams(players):     # Create our function 
    random.shuffle(players) # SHuffle the list of players
    team1 = players[:len(players) // 2] # put the first half of players into the first team
    teamCaption1 = team1[random.randrange(0,12)] #rabdomly assingn a team caption
    print("Team 1: ")
    print("Team 1 Caption: " + teamCaption1)
    for player in team1:
        print(player)

PickTeams(players)

team2 = players[:len(players) // 2]
teamCaption2 = team2[random.randrange(0,12)]
print("Team 2: ")
print("Team 2 Caption " + teamCaption2)
for player in team2:
    print(player)
    



