
print("FORWARD CHAINING")
print("Enter the facts (Yes/No):")

american = input("Is Robert an American? (yes/no): ").lower()
missile = input("Is M1 a Missile? (yes/no): ").lower()
enemy = input("Is Country A an Enemy of America? (yes/no): ").lower()
sell = input("Did Robert sell M1 to Country A? (yes/no): ").lower()

weapon = False
hostile = False
criminal = False

print("\nApplying Rules...\n")

# Rule 1
if missile == "yes":
    weapon = True
    print("Rule 1: Missile(M1) -> Weapon(M1)")
    print("M1 is a Weapon")

# Rule 2
if enemy == "yes":
    hostile = True
    print("Rule 2: Enemy(Country A) -> Hostile(Country A)")
    print("Country A is Hostile")

# Rule 3
if american == "yes" and weapon and hostile and sell == "yes":
    criminal = True
    print("Rule 3: American + Weapon + Hostile + Sell")
    print("Criminal(Robert)")

print("\nConclusion:")

if criminal:
    print("Robert is Criminal")
else:
    print("Cannot prove Robert is Criminal")
