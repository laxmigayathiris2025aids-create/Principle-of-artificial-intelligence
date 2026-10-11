
print("Traffic Rule Resolution")

print("\nTraffic Symbols")
print("P : Traffic Signal is RED")
print("Q : Vehicles must STOP")
print("R : Emergency Vehicle is Allowed")

print("\nEnter the Traffic Clauses")

clause1 = set(input("Enter Clause 1: ").split())
clause2 = set(input("Enter Clause 2: ").split())

resolvent = set()

for literal in clause1:

    # Find complement
    if literal.startswith("~"):
        complement = literal[1:]
    else:
        complement = "~" + literal

    # Apply Resolution
    if complement in clause2:

        resolvent = (clause1 - {literal}) | (clause2 - {complement})
        break

print("\nResolvent")
print(resolvent)

