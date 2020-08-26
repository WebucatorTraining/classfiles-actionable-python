_output = ""

def addheaders():
    # Write your code here
    pass

def addrow():
    # Write your code here

    # The rest of the function prompts the user to add another row
    # or quit. On quitting, it prints _output. Leave it as is.

    again = input("Again? Press ENTER to add a row or Q to quit. ")
    if again.lower() != "q":
        addrow()
    else:
        print(_output)

def main():
    # Call addheaders() and addrow()
    addheaders()
    addrow()

main()