from cats import cats

print("Welcome to Whiskers Adoption Hub!")

while True:
    print("\nSearch by:")
    print("1. Status")
    print("2. Breed")
    print("3. Age")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "4":
        print("Goodbye!")
        break

    search = input("Enter your search: ")

    print("\nSearch Results:")
    found = False

    for cat in cats:
        if (
            (choice == "1" and cat["status"].lower() == search.lower()) or
            (choice == "2" and cat["breed"].lower() == search.lower()) or
            (choice == "3" and str(cat["age"]) == search)
        ):
            print("Name:", cat["name"])
            print("Age:", cat["age"])
            print("Breed:", cat["breed"])
            print("Status:", cat["status"])
            print("-------------------------")
            found = True

    if not found:
        print("No matching cats found.")

