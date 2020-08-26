from pathlib import Path

def add_item(list_file, item):
    """Appends item (after stripping leading and trailing
    whitespace) to list_file followed by newline character

    Keyword arguments:
    list_file -- the path to the file
    item -- the item to append"""
    with open(list_file, 'a', encoding='utf-8') as f:
        f.write(item.strip() + '\n')

def remove_item(list_file, item):
    """Removes first instance of item from list_file
    If item is not found in list_file, alerts user.

    Keyword arguments:
    list_file -- the path to the file
    item -- the item to remove"""
    item_found = False
    with open(list_file, 'r', encoding='utf-8') as f:
        items = f.read().splitlines()
        if item in items:
            items.remove(item)
            item_found = True
        else:
            print('"' + item + '" not found in list.')

    if item_found:
        with open(list_file, 'w') as f:
            f.write('\n'.join(items) + '\n')

def delete_list(list_file):
    """Deletes the entire contents of list_file."""
    with open(list_file, 'w', encoding='utf-8') as f:
        print('The list has been deleted.')

def print_list(list_file):
    """Prints list in list_file."""
    with open(list_file, 'r', encoding='utf-8') as f:
        print(f.read())

def show_instructions():
    """Prints instructions"""
    print("""OPTIONS:
    P
        -- Print List
    +abc
        -- Add 'abc' to list
    -abc
        -- Remove 'abc' from list
    --all
        -- Delete entire list
    Q
        -- Quit\n""")

def main():
    show_instructions()
    list_file = Path('list.txt')

    while True:
        choice = input('>> ')

        if choice.lower() == 'q':
            print('Goodbye!')
            break

        if choice.lower() == 'p':
            print_list(list_file)
        elif choice.lower() == '--all':
            delete_list(list_file)
        elif choice and choice[0] == '+':
            add_item(list_file, choice[1:])
        elif choice and choice[0] == '-':
            remove_item(list_file, choice[1:])
        else:
            print("I didn't understand.")
            show_instructions()


if __name__ == '__main__':
    main()