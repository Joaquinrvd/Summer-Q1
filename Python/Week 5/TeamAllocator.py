


import random 


players = ["Devon", "Kauri", "Isaiah",
           "Braylen", "Taymur", "Xavier",
           "Avery", "Taqari", "Kenlon",
           "Marshawn", "Nahum", "Kamari",
           "Kristopher", "Joseph", "Darren", 
           "Carl", "Walter", "Jeffrey", 
           "Nishad", "Maximus", "Ja’Den", 
           "Jarmauri", "Eustace", "Semaj", "Joaquin"]

def pick_teams(players):
    random.shuffle(players)  
    half = len(players) // 2
    team1 = players[:half]         
    team2 = players[half:]        

    team_caption1 = random.choice(team1)  
    team_caption2 = random.choice(team2)  

    print("\nTeam 1:")
    print("Captain:", team_caption1)
    for player in team1:
        print("-", player)

    print("\nTeam 2:")
    print("Captain:", team_caption2)
    for player in team2:
        print("-", player)


while True:
    pick_teams(players)
    user_input = input("\nAre you happy with these teams? (yes/no): ").strip().lower()
    if user_input == "yes":
        print("Great! Teams are set.")
        break
    else:
        print("\nShuffling teams again...\n")
