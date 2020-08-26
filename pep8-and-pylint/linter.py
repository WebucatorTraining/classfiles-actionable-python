"""
    Install pylint:
        pip install pylint
    Run this with:
        python linter.py path_to_folder > pylint.txt
        e.g., python linter.py date-time/Exercises > pylint.txt
"""
import sys
import os
import pylint.lint

def file_path(relative_path):
    """Returns absolute path from relative path"""
    folder = os.path.dirname(os.path.abspath(__file__))
    path_parts = relative_path.split("/")
    new_path = os.path.join(folder, *path_parts)
    return new_path

def file_list(start_dir):
    files = []
    for dirpath, dirnames, filenames in os.walk(start_dir):
        if "venv" in dirpath:
            continue
        for fname in filenames:
            if os.path.splitext(fname)[1] == ".py":
                files.append(file_path(dirpath + '/' + fname))
    return files

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    print(path)
    files = file_list(path)

    pylint.lint.Run(files, do_exit=False)

main()
