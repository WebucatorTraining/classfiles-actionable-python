def get_inits(name):
    # Create list from first letter of each name part
    inits = [name_part[0] for name_part in name.split()]
    # Join inits list on "." and append "." to end
    return '.'.join(inits) + '.'

def main():
    people = ['George Washington', 'John Adams', 
              'Thomas Jefferson', 'John Quincy Adams']

    # Create list by mapping person elements to get_inits()
    inits = [get_inits(person) for person in people]
    print(inits)

main()