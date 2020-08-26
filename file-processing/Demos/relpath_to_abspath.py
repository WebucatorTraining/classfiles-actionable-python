import os

relative_path = "my_files/zen_of_python.txt"
print("__file__:", __file__)

# Get absolute path to Python script
abs_path = os.path.abspath(__file__)
print("abs_path:", abs_path)

# Get absolute path to the directory that the script is in
folder = os.path.dirname(abs_path)
print("dir:", folder)

# Split the relative path on the forward slash
path_parts = relative_path.split("/")
print("path_parts:", path_parts)

# Join dir with path_parts to get an absolute path to the file to open.
new_path = os.path.join(folder, *path_parts)
print("new_path:", new_path)