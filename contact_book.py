contacts = {}

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added successfully!")

    elif choice == "2":
        if not contacts:
            print("No contacts available.")
        else:
            print("Your Contacts:")
            for name, phone in contacts.items():
                print(f"{name} : {phone}")

    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"{name} : {contacts[name]}")
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
