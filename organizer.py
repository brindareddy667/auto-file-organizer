import os
import shutil

def organize_folder(target_dir):
    # Define categories and their extensions
    extensions = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Archives': ['.zip', '.tar', '.rar', '.7z'],
        'Scripts': ['.py', '.js', '.cpp', '.sql']
    }

    # Iterate through files in the target directory
    for filename in os.listdir(target_dir):
        file_path = os.path.join(target_dir, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, ext = os.path.splitext(filename)

        # Find the right folder for the extension
        for folder, ext_list in extensions.items():
            if ext.lower() in ext_list:
                folder_path = os.path.join(target_dir, folder)
                
                # Create folder if it doesn't exist
                os.makedirs(folder_path, exist_ok=True)
                
                # Move the file
                shutil.move(file_path, os.path.join(folder_path, filename))
                print(f"Moved: {filename} -> {folder}")

if __name__ == "__main__":
    # Organizes the current directory where the script is run
    organize_folder(".")
