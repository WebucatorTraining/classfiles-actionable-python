from pathlib import Path

def search(word, text):
    """Return list of tuples holding each line number and line text."""
    results = []
    for line in enumerate(text, 1):
        if line[1].find(word) >= 0:
            results.append(line)
    return results

def main():
    zop = Path('my_files/zen_of_python.txt')
    with open(zop, encoding='utf-8') as f:
        zop_lines = f.readlines()

    word = input('Enter search word: ')
    results = search(word, zop_lines)
    if not results:
        print(f'{word} was not found.')
        
    for result in results:
        print(f'{word} appears on line {result[0]}: {result[1]}', end='')

main()