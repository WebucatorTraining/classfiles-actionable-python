import re
import random

def clean_cuss(match):
    # Get the whole match
    cuss = match.group(0)
    # Generate a random list of characters the length of cuss
    chars = [random.choice('!@#$%^&*') for letter in cuss]
    # Return the list joined into a string
    return ''.join(chars)

def main():
    pattern = r'\b[a-z]*(stupid|stinky|darn|shucks|crud|slob)[a-z]*\b'
    p = re.compile(pattern, re.IGNORECASE|re.MULTILINE)
    s = """Shucks! What a cruddy day I\'ve had.
I spent the whole darn day with my slobbiest
friend darning his STINKY socks."""
    result = p.sub(clean_cuss, s)
    print(result)

main()