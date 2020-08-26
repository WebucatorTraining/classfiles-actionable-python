from pathlib import Path

a_dir = Path('my_files/a')
c_dir = a_dir / 'b/c'

a_dir.mkdir(exist_ok=True)
c_dir.mkdir(parents=True, exist_ok=True)

a_demo = a_dir / 'a-demo.txt'
a_demo.write_text('Dummy text', encoding='utf-8')

b_demo = a_dir / 'b/b-demo.txt'
b_demo.write_text('Dummy text', encoding='utf-8')

c_demo = c_dir / 'c-demo.txt'
c_demo.write_text('Dummy text', encoding='utf-8')