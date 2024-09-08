import os
def get_folder_size(directory):
    """Calculate the total size of the directory, including all subdirectories and files."""
    total_size = 0
    for root, dirs, files in os.walk(directory):
        for name in files:
            try:
                file_path = os.path.join(root, name)
                total_size += os.path.getsize(file_path)
            except PermissionError:
                continue
    return total_size

directory = "C:/Users/Note-Felipe/.pyenv"

#def list_files_and_folders(directory, progress_callback):
"""List files and folders with their sizes and modification dates."""
items = []
total_files = sum([len(files) for _, _, files in os.walk(directory)])
processed_files = 0

with os.scandir(directory) as it:
    for entry in it:
        if entry.is_file():
            path = entry.path
            size_bytes = entry.stat().st_size
            items.append((path, size_bytes))
            processed_files += 1
        elif entry.is_dir():
            path = entry.path
            size_bytes = get_folder_size(path)
            items.append((path, size_bytes))
            processed_files += 1
        
        total_files = len(items)
        progress = int((processed_files / total_files) * 100)
#        progress_callback(progress)  # Update progress bar

# Call the main function with the specified directory
print(progress)
