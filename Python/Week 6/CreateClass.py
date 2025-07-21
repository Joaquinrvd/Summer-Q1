# 1. Create a class to represent a video game or a movie collection 
# 2. Create a constructer method _init_()
# 3. Create a list for the vidoe games and moives each
# 4. Create a indtsnce variable for the user's favorite movie and video game respectivly 
# 5. Create a following functions for your class
# - A function to display all the movies 
# - A function to display all the video games
# - A function to add a movie/video game
# - A function to remove a movie/video game
# - A function to select a favorite video game and or movie 
# 6. Create a seporate tester.py file to test your code

class Collection:

    def __init__(self, movieList, gameList,):
        self.movieList = []
        self.gameList = []
        self.favGame = ""
        self.favMovie = ""

        self.movieList = movieList
        self.gameList = gameList

    def AddGame(self, game):
        if game in self.gameList:
            print("Game is already in list")
        else:
            self.gameList.append(game)

    def AddMovie(self, movie):
        if movie in self.movieList:
            print("Game is already in list")
        else:
            self.movieList.append(movie)

    def RemoveGame(self, game):
        if game in self.gameList:
            self.gameList.remove(game)
        else:
            print("Game Not Found")


    def RemoveMovie(self, movie):
        if movie in self.movieList:
            self.gameList.remove(movie)
        else:
            print("Movie Not Found")

    def DisplayGames(self):
        for game in self.gameList:
            print(game)

    def DisplayMovie(self):
        for movie in self.movieList:
            print(movie)
    
    def DisplayFavGame(self):
        print(f'Fav Game: {self.favGame}')

    def DisplayFavMovie(self):
        print(f'Fav Movie: {self.favMovie}')

    def DisplayCollection(self):
        self.DisplayGames()
        self.DisplayFavGame()
        self.DisplayMovie()
        self.DisplayFavMovie()

    def setfavmovie(self, movie):
        if movie not in self.movieList:
            self.AddMovie(movie)
        self.favMovie = movie

    def setfavgame(self, game):
        if game not in self.gameList:
            self.AddGame(game)
        self.favGame = game
