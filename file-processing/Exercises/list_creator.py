from pathlib import Path

def add_item(item):
    """Appends item (after stripping leading and trailing
    whitespace) to list.txt followed by newline character

    Keyword arguments:
    item -- the item to append"""
    pass

def remove_item(item):
    """Removes first instance of item from list.txt
    If item is not found in list.txt, alerts user.

    Keyword arguments:
    item -- the item to remove"""
    pass

def delete_list():
    """Deletes the entire contents of the list by opening
    list.txt for writing."""
    pass

def print_list():
    """Prints list"""
    pass

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

    while True:
        choice = input('>> ')

        if choice.lower() == 'q':
            print('Goodbye!')
            break

        if choice.lower() == 'p':
            print_list()
        elif choice.lower() == '--all':
            delete_list()
        elif choice and choice[0] == '+':
            add_item(choice[1:])
        elif choice and choice[0] == '-':
            remove_item(choice[1:])
        else:
            print("I didn't understand.")
            show_instructions()

if __name__ == '__main__':
    main()