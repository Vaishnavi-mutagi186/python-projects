import os
import shutil
import sys

def organize_folder(source_folder):
    if not os.path.exists(source_folder):
        print("❌ Folder path not found!")
        sys.exit()

    for file in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file)

        if os.path.isfile(file_path):

            file_lower = file.lower()

            if file_lower.endswith((".png", ".jpg", ".jpeg")):
                folder = "Images"

            elif file_lower.endswith((".pdf", ".docx", ".txt")):
                folder = "Documents"

            elif file_lower.endswith((".mp4", ".avi")):
                folder = "Videos"

            else:
                folder = "Others"

            dest = os.path.join(source_folder, folder)
            os.makedirs(dest, exist_ok=True)

            shutil.move(file_path, os.path.join(dest, file))

    print("✅ Files organized successfully!")

# Main program
if __name__ == "__main__":
    source_folder = input("Enter folder path to organize: ").strip('"')
    organize_folder(source_folder)