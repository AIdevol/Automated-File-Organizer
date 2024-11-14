
import os
import shutil
from datetime import datetime

def categorize_file(filepath):
    filename, extension = os.path.splitext(filepath)
    categories = {
        ".jpg": "images",
        ".png": "images",
        ".pdf": "documents",
        ".docx": "documents",
        ".mp4": "videos",
        ".avi": "videos",
        ".mkv": "videos",
        ".exe": "apps"
    }
    return categories.get(extension.lower(), "other")

def create_folders(directory):
    os.makedirs(os.path.join(directory, "images"), exist_ok=True)
    os.makedirs(os.path.join(directory, "documents"), exist_ok=True)
    os.makedirs(os.path.join(directory, "videos"), exist_ok=True)
    os.makedirs(os.path.join(directory, "other"), exist_ok=True)
    os.makedirs(os.path.join(directory, "apps"), exist_ok=True)

def sort_files(source_directory, target_directory):
    for root, _, files in os.walk(source_directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_category = categorize_file(filename)
            target_path = os.path.join(target_directory, file_category, filename)
            try:
                shutil.copy2(filepath, target_path)
                file_date = datetime.fromtimestamp(os.path.getmtime(filepath))
                
                # Replace colons to avoid invalid filename errors
                sanitized_date = file_date.isoformat().replace(":", "-")
                new_filename = f"{sanitized_date}-{filename}"
                
                os.rename(target_path, os.path.join(os.path.dirname(target_path), new_filename))
            except Exception as e:
                print(f"Error moving '{filepath}': {e}")

def main():
    source_directory = input("Sorry to bother you Lord Vinson, but I'll need the source directory:")
    target_directory = input("Sorry to bother you once again Lord Vader, but I'll need the destination directory:")

    create_folders(target_directory)
    sort_files(source_directory, target_directory)

    print("File organization completed!")

if __name__ == "__main__":
    main()
