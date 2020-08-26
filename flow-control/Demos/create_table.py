import keyword

def create_table(item_list, num_cols):
    table = ''
    for num, item in enumerate(item_list):
        table += f'{item:10}'
        if num % num_cols == num_cols - 1:
            table += '\n'

    return table

def main():
    table = create_table(keyword.kwlist, 5)
    print(table)

main()