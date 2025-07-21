import CreateClass

movies = ["idk", "I dont watch movies", "i really dont know"]
games = ["Sekiro: Shadows Die Twice", "Elden Ring", "Subnautica"]

myCollection = CreateClass.Collection(movies, games)

myCollection.setfavgame("Sekiro: Shadows Die Twice")
myCollection.setfavmovie("idk")
myCollection.DisplayCollection()