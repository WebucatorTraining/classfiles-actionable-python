from collections import Counter

with open('Declaration_of_Independence.txt') as f:
    doi = f.read()

word_list = [word for word in doi.upper().split() if len(word) > 5]
    
c = Counter(word_list)
print(c.most_common(10))