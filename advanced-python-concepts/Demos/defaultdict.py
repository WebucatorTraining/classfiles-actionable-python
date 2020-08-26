from collections import defaultdict

dice_rolls = [(a,b)
              for a in range(1,7)
              for b in range(1,7)]

roll_counts = defaultdict(int)
for roll in dice_rolls:
    roll_counts[sum(roll)] += 1