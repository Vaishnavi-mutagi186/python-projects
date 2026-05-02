import hashlib
import os

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed = hash_password(password)

    with open("users.txt", "a") as file:
        file.write(f"{username}:{hashed}\n")

    print("Registration successful!\n")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed = hash_password(password)

    if not os.path.exists("users.txt"):
        print("No users registered yet.\n")
        return

    with open("users.txt", "r") as file:
        for line in file:
            saved_user, saved_hash = line.strip().split(":")
            if username == saved_user and hashed == saved_hash:
                print("Login successful ✅\n")
                return

    print("Invalid username or password ❌\n")

while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice\n")
