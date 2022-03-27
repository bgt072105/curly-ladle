
# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list
InfoDb.append({
    "FirstName": "Brian",
    "LastName": "Tang",
    "FavoriteSport": "Tennis",
    "FavoriteColor": "Blue",
    "FavoriteAnimal": "Dog",
    "CountriesYouWantToTravelTo":["Germany", "Sweden", "United Kingdom", "Poland", "Iceland"]
})

InfoDb.append({
    "FirstName": "Justin",
    "LastName": "Nguyen",
    "FavoriteSport": "Soccer",
    "FavoriteColor": "Green",
    "FavoriteAnimal": "Cat",
    "CountriesYouWantToTravelTo":["Mexico", "Brazil", "Argentina", "Chile", "Bolivia"]
})

InfoDb.append({
    "FirstName": "Noah",
    "LastName": "Israel",
    "FavoriteSport": "Hockey",
    "FavoriteColor": "Yellow",
    "FavoriteAnimal": "Giraffe",
    "CountriesYouWantToTravelTo":["South Africa", "Tazania", "Rwanda", "Nigeria", "Ghana"]
})

InfoDb.append({
    "FirstName": "Diba",
    "LastName": "Vazirian",
    "FavoriteSport": "Baseball",
    "FavoriteColor": "Purple",
    "FavoriteAnimal": "Rhino",
    "CountriesYouWantToTravelTo":["China", "Vietnam", "Korea", "Japan", "Thailand"]
})

InfoDb.append({
    "FirstName": "Hailey",
    "LastName": "Chau",
    "FavoriteSport": "Football",
    "FavoriteColor": "Red",
    "FavoriteAnimal": "Lizard",
    "CountriesYouWantToTravelTo":["Belgium", "Greenland", "India", "Australia", "New Zealand"]
})

# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t","Favorite Sport: ", InfoDb[n]["FavoriteSport"])
    print("\t","Favorite Color: ", InfoDb[n]["FavoriteColor"])
    print("\t","Favorite Animal: ", InfoDb[n]["FavoriteAnimal"])
    print("\t", "Countries they want to travel to: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["CountriesYouWantToTravelTo"]))  # join allows printing a string list with separator
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)

## hack 2b: def while_loop(0)
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

## hack 2c : def recursive_loop(0)
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return

def infoDB():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion

if __name__ == "__main__":
    infoDB()