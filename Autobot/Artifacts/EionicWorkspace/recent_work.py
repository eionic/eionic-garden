import os
import datetime

def get_recently_modified_files(directory, days=7):
    recently_modified_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            if (datetime.datetime.now() - modified_date).days <= days:
                recently_modified_files.append(file_path)
    return recently_modified_files

recently_modified_files = get_recently_modified_files('.')

print("Recently modified files:")
for file in recently_modified_files:
    print(file)