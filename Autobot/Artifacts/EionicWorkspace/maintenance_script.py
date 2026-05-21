import os
import time

def get_recently_modified_files(directory, num_files):
    """
    Returns a list of the most recently modified files in the given directory.
    
    Args:
        directory (str): The directory to search for files.
        num_files (int): The number of files to return.
    
    Returns:
        list: A list of tuples containing the file name and modification time.
    """
    files = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            modification_time = os.path.getmtime(filepath)
            files.append((filename, modification_time))
    
    # Sort the files by modification time in descending order
    files.sort(key=lambda x: x[1], reverse=True)
    
    # Return the most recently modified files
    return files[:num_files]

def main():
    directory = '/path/to/directory'
    num_files = 5
    recently_modified_files = get_recently_modified_files(directory, num_files)
    
    print("Recently modified files:")
    for filename, modification_time in recently_modified_files:
        print(f"{filename} - {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modification_time))}")

if __name__ == "__main__":
    main()