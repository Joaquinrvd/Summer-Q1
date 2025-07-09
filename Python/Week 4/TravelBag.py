#1. Create a list of items in your room you can potentially pack.
#2. Create an empty list to represent your travel bag 
#3. Repeatedly prompt the user for items to put in their travel bag by removing them from the the list of items in your room to your travel bag list.
#4. Once the list is complete, finalize it by creating a tuple representing your luggage. It should have every item in your travel bag. Empty the travel bag list as you do this.
#5. Print the contents of your luggage for the trip, as well as the number of items you decided to bring

Bedroom = ["day shirts", "day pants", "pairs of pajamas", "3 pairs of shoes",
            "toothbrush & toothpaste", "hair products", "combs",
            "chargers", "games", "laptop", "headphones",]

TravelBag = []

print("PACK YOUR BAGS")
print("Enter the index of the item you would like to move from your room to your Bag")
print("Type '100' when you are done packing")
print(" ")
print("Your Bedroom items:")
print(Bedroom)

items = int(input("Item Index: "))

while items != 100:
    TravelBag.append(Bedroom[items])
    Bedroom.remove(Bedroom[items])
    print("\nYour Bedroom")
    print(Bedroom)
    print("\nYour Travel Bag")
    print(TravelBag)
    items = int(input("Item Index: "))

print("\nYour finished luggage: ")
for items in TravelBag:
    print(items)