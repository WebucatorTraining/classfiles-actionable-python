from pathlib import Path

yoda = Path('my_files/yoda.txt')
with open(yoda, 'a+', encoding='utf-8') as f:
    f.write('Powerful you have become.')
    print(f.read())