def say_hello():
    your_name = input("What is your name? ")
    insert_separator()
    print("Hello, ", your_name, "!", sep="")

def insert_separator():
    print("===")

def recite_poem():
    print("How about a Monty Python poem?")
    insert_separator()
    print("Much to his Mum and Dad's dismay")
    print("Horace ate himself one day.")
    print("He didn't stop to say his grace,")
    print("He just sat down and ate his face.")

def say_goodbye():
    print("Goodbye!")

def main():
    say_hello()
    insert_separator()
    recite_poem()
    insert_separator()
    say_goodbye()

main()