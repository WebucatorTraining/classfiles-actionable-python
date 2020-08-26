dice_rolls = [(a,b)
              for a in range(1,7)
              for b in range(1,7)]
              
roll_counts = {}
for roll in dice_rolls:
    try:
        roll_counts[sum(roll)] += 1
    except KeyError:
        roll_counts[sum(roll)] = 1