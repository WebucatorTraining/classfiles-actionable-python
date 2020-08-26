output = 'Char\tisdigit\tisdecimal\tisnumeric'
html_output = '''<table border="1">
<thead>
    <tr>
        <th>Char</th>
        <th>isdigit</th>
        <th>isdecimal</th>
        <th>isnumeric</th>
    </tr>
</thead>
<tbody>'''

for i in range(1, 1114111):
    if chr(i).isdigit() or chr(i).isdecimal() or chr(i).isnumeric():
        output += f'\n{chr(i)}\t{chr(i).isdigit()}'
        output += f'\t{chr(i).isdecimal()}\t{chr(i).isnumeric()}'

        if not (chr(i).isdigit() and chr(i).isdecimal() and chr(i).isnumeric()):
            # one is False
            color = 'red'
        else:
            color = 'black'

        html_output += f'''<tr style="color:{color}">
     <td>{chr(i)}</td>   
     <td>{chr(i).isdigit()}</td>   
     <td>{chr(i).isdecimal()}</td>   
     <td>{chr(i).isnumeric()}</td>   
</tr>'''

html_output += '</tbody></table>'

with open('numbers.txt', 'w', encoding="utf-8") as f:
    f.write(output)

print('Look in the strings/Demos directory for a new file.')

with open('numbers.html', 'w', encoding="utf-8") as f:
    f.write(html_output)

print('''Look in the strings/Demos directory for new \
numbers.txt and numbers.html files.''')