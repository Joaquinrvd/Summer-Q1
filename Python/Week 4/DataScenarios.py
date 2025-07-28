# DataScenarios.py
# Python / Week4
# Demonstration of best data structures: List, Tuple, Dictionary, Set

#1. A restaurant menu with prices for each item
print("Scenario #1: A restaurant menu with prices for each item.")
print("Best Structure: Dictionary; best way to pair prices with the items.")
menu = {
    "French Toast": 12,
    "Grand Slam": 12,
    "T-Bone": 18,
    "Avocado Toast": 15
}
for key, item in menu.items():
    print(key, ": $", item)

#2. High scores to an arcade game
print("\nScenario #2: High scores to an arcade game.")
print("Best Structure: List; scores change often and order matters.")
high_scores = [100, 105, 110, 99]
for score in high_scores:
    print(score)

#3. All of the months of the year
print("\nScenario #3: All of the months of the year.")
print("Best Structure: Tuple; months are fixed and unchangeable.")
months = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
)
for month in months:
    print(month)

#4. All the items in your backpack
print("\nScenario #4: All the items in your backpack.")
print("Best Structure: Set; no duplicate items, order doesn't matter.")
backpack_items = {"Notebook", "Pencil", "Laptop", "Charger", "Water Bottle"}
for item in backpack_items:
    print(item)

#5. Look up Student emails by their names
print("\nScenario #5: Look up student emails by their names.")
print("Best Structure: Dictionary; allows fast lookups by name.")
student_emails = {
    "Alice": "alice@example.com",
    "Bob": "bob@example.com",
    "Charlie": "charlie@example.com"
}
for name, email in student_emails.items():
    print(name, "->", email)

#6. A shopping cart of groceries
print("\nScenario #6: A shopping cart of groceries.")
print("Best Structure: List; ordered, can contain duplicates (e.g., 2 apples).")
shopping_cart = ["Apple", "Banana", "Milk", "Apple", "Bread"]
for item in shopping_cart:
    print(item)

#7. Scenario: List of favorite programming languages
print("\nScenario #7: List of favorite programming languages.")
print("Best Structure: Set; only unique languages, no duplicates.")
favorite_languages = {"Python", "JavaScript", "C++", "Python", "Get.do"}
for lang in favorite_languages:
    print(lang)
