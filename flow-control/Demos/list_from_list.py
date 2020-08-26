def initials(name):
    fullname = name.split(' ')
    inits = (fullname[0][0], fullname[1][0])
    return inits

def main():
    names = ['Graham Chapman', 'John Cleese', 'Eric Idle',
             'Terry Gilliam', 'Terry Jones', 'Michael Palin']
    inits = [initials(name) for name in names]
    for i in inits:
        print(f'{i[0]}.{i[1]}.')

main()