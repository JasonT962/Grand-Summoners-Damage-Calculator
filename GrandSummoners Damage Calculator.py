#This is the attack of your unit + enhanced attack from tasmons and luck buff
BaseAttack = 0

#All attack% buffs are additive so if character has 50% attack up and an equipment has 50% attack up, that's 100% attack up in total
AttackUp = 0

#Just read off the unit's skill/arts multiplier and put it here
SkillMultiplier = 0

#Damage up is in percentage, this is additive with all sources of damage up buffs such as crit damage up and arts damage up. But don't include crit damage here
DamageUp = 0

CritDamageUp = 0

#Debuff to enemy applying resistance down or damage to enemy up, this is additive e.g. Physical res down 50% + water res down 50% + Mako Arts DMGtoEnemyUp 30% = 130% res down
ResistanceDown = 0

# Any buff/debuff that reduces enemy's defence or ignores enemy's defence
DefenceDown = 0


# Enemy Stats (Optional)

EnemyResistance = 0


EnemyDefence = 0


#Ignore the rest of this code unless you know what you're doing

attack = BaseAttack * ((AttackUp/100)+1)

EnemyDefence = EnemyDefence * (1-(DefenceDown/100))

TotalResistance = 1 + ((ResistanceDown-EnemyResistance)/100)
if TotalResistance <= 0:
    TotalResistance = 0

def Damage():
    return ((attack/10)*(2-((attack*2)/(attack+3500))))*(SkillMultiplier/100) * ((DamageUp/100)+1) * TotalResistance * (1-(EnemyDefence/(EnemyDefence+5000)))

def critDamage():
    return ((attack/10)*(2-((attack*2)/(attack+3500))))*(SkillMultiplier/100) * (((DamageUp+CritDamageUp)/100)+1) * TotalResistance * 1.25


print("Damage:",Damage())
print("Crit Damage:",critDamage())
