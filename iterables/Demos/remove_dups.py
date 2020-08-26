def main():
    veggies = ["tomato", "spinach", "pepper", "pea", "tomato", "pea"]
    v_set = set(veggies) # turn list into set removing dups
    print(v_set) # {"pepper", "tomato", "spinach", "pea"}

    veggies = list(v_set) # turn set back into a list
    print(veggies) # ["pepper", "tomato", "spinach", "pea"]

main()