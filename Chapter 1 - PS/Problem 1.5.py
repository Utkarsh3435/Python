import os

# Specify the directory path
directory_path = '/Python'

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print the contents
for item in contents:
    print(item)
