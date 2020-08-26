_output = ""

def add_headers():
    global _output
    c_header = f"{'Company':^10}"
    r_header = f"{'Revenue':^10}"
    e_header = f"{'Expenses':^10}"
    p_header = f"{'Profit':^10}"
    _output += f"{c_header}\t{r_header}\t{e_header}\t{p_header}\n"

def add_row():
    global _output

    c = input("Company: ")
    r = float(input("Revenue: "))
    e = float(input("Expenses: "))
    p = r - e # profit

    c_str = f"{c:<10}"
    r_str = f"${r:>10,.2f}"
    e_str = f"${e:>10,.2f}"
    p_str = f"${p:>10,.2f}"

    new_row = f"{c_str}\t{r_str}\t{e_str}\t{p_str}\n"

    _output += new_row

    again = input("Again? Press ENTER to add a row or Q to quit. ")
    if again.lower() != "q":
        add_row()
    else:
        print(_output)

def main():
    add_headers()
    add_row()

main()