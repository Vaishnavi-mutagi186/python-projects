import random
import json
import os

FILE_NAME = "quotes.json"

# Default quotes (used if file doesn't exist)
default_quotes = [
    {"quote": "Believe in yourself.", "author": "Unknown", "category": "Motivation"},
    {"quote": "Stay hungry, stay foolish.", "author": "Steve Jobs", "category": "Success"},
    {"quote": "Dream big and dare to fail.", "author": "Norman Vaughan", "category": "Dream"},
    {"quote": "Push yourself, because no one else will.", "author": "Unknown", "category": "Motivation"}
]


# Load quotes from file
def load_quotes():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            json.dump(default_quotes, f, indent=4)

    with open(FILE_NAME, "r") as f:
        return json.load(f)


# Save quotes to file
def save_quotes(quotes):
    with open(FILE_NAME, "w") as f:
        json.dump(quotes, f, indent=4)


# Get random quote
def get_random_quote(quotes):
    quote = random.choice(quotes)
    print(f'\n💡 "{quote["quote"]}"')
    print(f'   — {quote["author"]} [{quote["category"]}]\n')


# Filter by category
def get_by_category(quotes):
    category = input("Enter category: ")
    filtered = [q for q in quotes if q["category"].lower() == category.lower()]

    if filtered:
        quote = random.choice(filtered)
        print(f'\n💡 "{quote["quote"]}"')
        print(f'   — {quote["author"]} [{quote["category"]}]\n')
    else:
        print("❌ No quotes found for this category.")


# Add new quote
def add_quote(quotes):
    text = input("Enter quote: ")
    author = input("Enter author: ")
    category = input("Enter category: ")

    new_quote = {
        "quote": text,
        "author": author,
        "category": category
    }

    quotes.append(new_quote)
    save_quotes(quotes)
    print("✅ Quote added successfully!")


# Main menu
def main():
    quotes = load_quotes()

    while True:
        print("\n--- Random Quote Generator ---")
        print("1. Get Random Quote")
        print("2. Get Quote by Category")
        print("3. Add New Quote")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            get_random_quote(quotes)

        elif choice == "2":
            get_by_category(quotes)

        elif choice == "3":
            add_quote(quotes)
            quotes = load_quotes()  # reload after adding

        elif choice == "4":
            print("Goodbye 👋")
            break

        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()
