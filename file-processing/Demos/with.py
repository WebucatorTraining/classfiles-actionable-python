from pathlib import Path

zop = Path('my_files/zen_of_python.txt')
with open(zop, encoding='utf-8') as f:
    poem = f.read()

# The file is now closed, but we saved its content in the poem variable
for i, line in enumerate(poem.splitlines(), 1):
    print(f"{i}. {line}")