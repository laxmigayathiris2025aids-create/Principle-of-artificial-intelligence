
print("BACKWARD CHAINING")
print("Prove that Robert is a Criminal")
print()

facts = {}

facts["American"] = input(
    "Is Robert an American? (yes/no): "
).lower()

facts["Missile"] = input(
    "Does Country A have missiles? (yes/no): "
).lower()

facts["Enemy"] = input(
    "Is Country A an enemy of America? (yes/no): "
).lower()

facts["Sells"] = input(
    "Did Robert sell missiles to Country A? (yes/no): "
).lower()


def prove(goal):

    if goal == "Criminal":
        print("\nGoal: Is Robert a Criminal?")

        return (
            prove("American")
            and prove("Weapon")
            and prove("Hostile")
            and prove("Sells")
        )

    elif goal == "American":
        print("Checking: Robert is an American")
        return facts["American"] == "yes"

    elif goal == "Weapon":
        print("Checking: Missiles are weapons")
        return facts["Missile"] == "yes"

    elif goal == "Hostile":
        print("Checking: Country A is hostile")
        return facts["Enemy"] == "yes"

    elif goal == "Sells":
        print("Checking: Robert sold missiles")
        return facts["Sells"] == "yes"

    return False


if prove("Criminal"):
    print("\nRobert is a Criminal.")
else:
    print("\nRobert is NOT proven to be a Criminal.")
