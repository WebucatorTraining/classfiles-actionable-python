import math

def main():
    people = int(input("How many people are eating? "))
    slices_per_person = float(input("How many slices per person? "))
    slices = slices_per_person * people

    slices_per_pie = int(input("How many slices per pie? "))
    pizzas = math.ceil(slices / slices_per_pie)

    print("You need", pizzas, "pizzas to feed", people, "people.")

    total_slices = slices_per_pie * pizzas
    slices_left = total_slices - slices
    print("There will be", slices_left, "leftover slices.")

main()