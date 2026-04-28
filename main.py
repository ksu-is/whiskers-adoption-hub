from cats import cats

print("Welcome to Whiskers Adoption Hub!")
print("Cats in our adoption system:\n")

for cat in cats:
    print("Name:", cat["name"])
    print("Age:", cat["age"])
    print("Breed:", cat["breed"])
    print("Status:", cat["status"])

    search = input("\nEnter a status to search for Available, Pending, or Adopted: ")

print("\nSearch Results:")
found = False

for cat in cats:
    if cat["status"].lower() == search.lower():
        print(cat["name"], "-", cat["breed"], "-", cat["status"])
        found = True

if not found:
    print("No cats found with that status.")

