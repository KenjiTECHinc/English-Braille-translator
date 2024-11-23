import os

def rename_directories(path):
    try:
        # List all items in the given directory path
        for directory in os.listdir(path):
            old_name = os.path.join(path, directory)
            # Check if it's a directory and has "_L" suffix
            if os.path.isdir(old_name) and directory.endswith("_L"):
                # New name without "_L"
                new_name = os.path.join(path, directory[:-2])
                # Rename the directory
                os.rename(old_name, new_name)
                print(f'Renamed: {old_name} -> {new_name}')
    except Exception as e:
        print(f"Error: {e}")

# Specify the path to the directory containing the folders
directory_path = "data/raw/character_set3/"
rename_directories(directory_path)
