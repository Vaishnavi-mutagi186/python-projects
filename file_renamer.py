import os

folder_path = input("Enter folder path: ")

files = os.listdir(folder_path)
count = 1

for file in files:
    old_path = os.path.join(folder_path, file)

    if os.path.isfile(old_path):
        new_name = f"file_{count}{os.path.splitext(file)[1]}"
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)
        count += 1

print("Files renamed successfully!")
