from collections import Counter
c = Counter(['green','blue','blue','red','yellow','green','blue'])
print('Colors Counter:', c, sep='\n', end='\n\n')

dice_rolls = [(a,b)
              for a in range(1,7)
              for b in range(1,7)]

roll_sums = [sum(roll) for roll in dice_rolls]
c = Counter(roll_sums)
print('Dice Roll Counter:', c, sep='\n')