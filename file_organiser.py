import os
import shutil
from pathlib import Path

# Define file type folders
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Videos': ['.mp4', '.avi', '.mov'],
    'Audio': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.sh'],
}

def organise_files(folder_path):
    """
    Organises files in the specified folder into subfolders based on their file types.
    
    :param folder_path: Path to the folder to organise.
    """

    # Create a Path object for the folder
    folder = Path(folder_path)
    
    # Check if the folder exists
    if not folder.exists():
        print(f"The specified path '{folder_path}' is invalid.")
        return
    
    # Move files to their respective folders
    for file in folder.iterdir():
        if file.is_file():
            moved = False
            for category, extensions in FILE_CATEGORIES.items():
                if file.suffix.lower() in extensions:
                    target_folder = folder / category
                    target_folder.mkdir(exist_ok=True)
                    shutil.move(str(file), str(target_folder / file.name))
                    print(f"Moved {file.name} to {category}/")
                    moved = True
                    break
            if not moved:
                other_dir = folder / 'Others'
                other_dir.mkdir(exist_ok=True)
                shutil.move(str(file), str(other_dir / file.name))
                print(f"Moved {file.name} to Others/")


if __name__ == "__main__":
    # Example usage
    path = input("Enter the path of the folder to organise: ")
    organise_files(path)
    # print("File organisation complete.")
