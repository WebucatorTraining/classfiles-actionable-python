from pathlib import Path

def file_path(relative_path):
    start_dir = Path(__file__).parent
    return Path(start_dir, relative_path)

zop = Path('my_files/zen_of_python.txt')
path_to_file = file_path(zop)
with open(path_to_file, encoding='utf-8') as f:
    poem = f.read()

for i, line in enumerate(poem.splitlines(), 1):
    print(f"{i}. {line}")