import shutil
import os
from datetime import datetime

def backup_file():
    filename = input("Enter file name to backup: ")

    if not os.path.exists(filename):
        print("File not found!\n")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}_{filename}"

    shutil.copy(filename, backup_name)
    print(f"Backup created: {backup_name}\n")

def restore_file():
    backup_file = input("Enter backup file name to restore: ")

    if not os.path.exists(backup_file):
        print("Backup file not found!\n")
        return

    original_name = "_".join(backup_file.split("_")[2:])
    shutil.copy(backup_file, original_name)
    print("File restored successfully ✅\n")

while True:
    print("1. Backup File")
    print("2. Restore File")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        backup_file()
    elif choice == "2":
        restore_file()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice\n")
   
