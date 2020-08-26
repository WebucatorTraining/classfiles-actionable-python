def divide():
    try:
        numerator = int(input('Enter a numerator: '))
        denominator = int(input('Enter a denominator: '))
        result = numerator / denominator
        print(numerator, 'over', denominator, 'equals', result)
    except ValueError:
        print('Integers only please. Try again.')
        divide()
    except ZeroDivisionError:
        print('You cannot divide by zero! Try again.')
        divide()
    except KeyboardInterrupt:
        print('Quitter!')
    except:
        print('I have no idea what went wrong!')

def main():
    divide()

main()