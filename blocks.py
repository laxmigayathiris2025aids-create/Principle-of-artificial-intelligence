
print("BLOCKS WORLD USING STRIPS")

# Initial State
initial_state = [
    "ONTABLE(A)",
    "ONTABLE(B)",
    "ONTABLE(C)",
    "CLEAR(A)",
    "CLEAR(B)",
    "CLEAR(C)",
    "ARMEMPTY"
]

print("\nInitial State:")
for fact in initial_state:
    print(fact)

# Goal State
goal_state = ["ON(A,B)", "ON(B,C)"]

print("\nGoal State:")
for fact in goal_state:
    print(fact)

# STRIPS actions
actions = [
    {
        "name": "PICKUP(B)",
        "preconditions": ["ONTABLE(B)", "CLEAR(B)", "ARMEMPTY"],
        "delete": ["ONTABLE(B)", "CLEAR(B)", "ARMEMPTY"],
        "add": ["HOLDING(B)"]
    },
    {
        "name": "STACK(B,C)",
        "preconditions": ["HOLDING(B)", "CLEAR(C)"],
        "delete": ["HOLDING(B)", "CLEAR(C)"],
        "add": ["ON(B,C)", "CLEAR(B)", "ARMEMPTY"]
    },
    {
        "name": "PICKUP(A)",
        "preconditions": ["ONTABLE(A)", "CLEAR(A)", "ARMEMPTY"],
        "delete": ["ONTABLE(A)", "CLEAR(A)", "ARMEMPTY"],
        "add": ["HOLDING(A)"]
    },
    {
        "name": "STACK(A,B)",
        "preconditions": ["HOLDING(A)", "CLEAR(B)"],
        "delete": ["HOLDING(A)", "CLEAR(B)"],
        "add": ["ON(A,B)", "CLEAR(A)", "ARMEMPTY"]
    }
]

print("\nSTRIPS PLAN")

state = initial_state.copy()

for i, action in enumerate(actions, 1):
    print("\nStep", i)
    print("Action:", action["name"])
    print("Preconditions:", ", ".join(action["preconditions"]))
    print("Delete:", ", ".join(action["delete"]))
    print("Add:", ", ".join(action["add"]))

    for fact in action["preconditions"]:
        if fact not in state:
            print("Action cannot be performed:", fact)
            break
    else:
        for fact in action["delete"]:
            if fact in state:
                state.remove(fact)

        for fact in action["add"]:
            if fact not in state:
                state.append(fact)

print("\nGoal State Achieved:")
for goal in goal_state:
    if goal in state:
        print(goal)
    else:
        print(goal, "not achieved")

if all(goal in state for goal in goal_state):
    print("\nAll goals achieved successfully!")
else:
    print("\nGoal state not achieved.")
