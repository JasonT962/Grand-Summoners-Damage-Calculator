# Grand Summoners Enemy Defence Calculator

# This is the damage you got from your calculator (no crit, enemy defence = 0)
NoDefDamage = 0

# This is the actual damage you see in game
DefDamage = 0



# Calculations - Ignore unless you know what you're doing

# Defence formula is:
# NoDefDamage * (1-ReductionRate) = DefDamage
# ReductionRate = 1-(DefDamage/NoDefDamage)
# ReductionRate = Defence/(Defence+5000)
# Defence = (5000*ReductionRate) / (1-ReductionRate)


ReductionRate = 1 - (DefDamage/NoDefDamage)

Defence = (5000*ReductionRate) / (1-ReductionRate)

print(Defence)

