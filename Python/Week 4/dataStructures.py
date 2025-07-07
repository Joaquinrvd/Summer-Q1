favsnacks = ["Twix", "Watermelon", "oreo's", "fruit snacks", "lays chips"]
favsnacks.append("Twix")
for snacks in favsnacks:
    print(snacks)



colleges = ("MIT", "Stanford", "Howard", "UC Berkeley", "Caltech")
for college in colleges:
    print(college)



spaceInfo = {
    "Moon landing: 1969",
    "Voyager 1 : 1977",
    "Hubble launched: 1990",
    "Mars Perseverance landed: 2021",
    "First private moon mission: 2023"
}
for Info in spaceInfo:
    print(Info)

carInfo = {
    "make":"Toyota",
    "model": "Camry",
    "year": 2022,
    "fuel_type": "Hybrid"
}
for car in carInfo:
    print(carInfo.get(car))