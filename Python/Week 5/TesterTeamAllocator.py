from TeamAllocator2 import TeamRandom

class TeamManager:
    def __init__(self):
        self.team_random = TeamRandom()

    def shuffle_teams(self):
        self.team_random.shuffle_teams()

    def assign_captains(self):
        self.team_random.assign_captains()

    def display_teams(self):
        self.team_random.display_teams()

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


