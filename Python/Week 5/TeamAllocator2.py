

import random

players = ["Devon", "Kauri", "Isaiah",
           "Braylen", "Taymur", "Xavier",
           "Avery", "Taqari", "Kenlon",
           "Marshawn", "Nahum", "Kamari",
           "Kristopher", "Joseph", "Darren", 
           "Carl", "Walter", "Jeffrey", 
           "Nishad", "Maximus", "Ja’Den", 
           "Jarmauri", "Eustace", "Semaj", "Joaquin"]

class TeamRandom:
    def __init__(self, players):
        self.players = players
        self.team1 = []
        self.team2 = []
        self.team_caption1 = None
        self.team_caption2 = None

    def shuffle_teams(self):
        random.shuffle(self.players)
        half = len(self.players) // 2
        self.team1 = self.players[:half]
        self.team2 = self.players[half:]

    def assign_captains(self):
        self.team_caption1 = random.choice(self.team1)
        self.team_caption2 = random.choice(self.team2)

    def display_teams(self):
        print("\nTeam 1:")
        print("Captain:", self.team_caption1)
        for player in self.team1:
            print("-", player)

        print("\nTeam 2:")
        print("Captain:", self.team_caption2)
        for player in self.team2:
            print("-", player)

    def print_teams_loop(self):
        while True:
            self.shuffle_teams()
            self.assign_captains()
            self.display_teams()

            user_input = input("\nAre you happy with these teams? (yes/no): ").strip().lower()
            if user_input == "yes":
                print("Great! Teams are set.")
                break
            else:
                print("\nShuffling teams again...\n")



team_randomizer = TeamRandom(players)
team_randomizer.print_teams_loop()
