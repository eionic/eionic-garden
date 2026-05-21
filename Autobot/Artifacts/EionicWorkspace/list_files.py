import os

def list_files(workspace_dir):
    try:
        files_and_dirs = os.listdir(workspace_dir)
        return files_and_dirs
    except FileNotFoundError:
        print(f"Workspace directory '{workspace_dir}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def main():
    workspace_dir = os.getcwd()
    files_and_dirs = list_files(workspace_dir)
    print("Files and directories in the workspace:")
    for file_or_dir in files_and_dirs:
        print(file_or_dir)

if __name__ == "__main__":
    main()