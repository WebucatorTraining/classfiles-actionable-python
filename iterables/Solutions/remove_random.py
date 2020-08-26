import random

def remove_random(the_list):
    x = random.choice(the_list)
    the_list.remove(x)
    return x

def main():
    colors = ['red', 'blue', 'green', 'orange']
    removed_color = remove_random(colors)
    print(f'The removed color was {removed_color}.')
    print(f'The remaining colors are {colors}.')

main()