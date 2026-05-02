tasks = []

while True:
    print("\nSimple CLI TODO List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print(f"Task '{task}' added successfully!")

    elif choice == "2":
        if tasks:
            print("Your Tasks:")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")
        else:
            print("No tasks yet!")

    elif choice == "3":
        print("Exiting TODO List. Bye!")
        break

    else:
        print("Invalid option. Please choose 1, 2 or 3.")
