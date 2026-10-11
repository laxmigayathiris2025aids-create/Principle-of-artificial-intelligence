
import heapq

# Graph with edge costs
graph = {
    'S': [('A', 4), ('B', 10), ('C', 11)],
    'A': [('B', 8), ('D', 5)],
    'B': [('D', 15)],
    'C': [('D', 8), ('E', 20), ('F', 2)],
    'D': [('H', 16), ('I', 20), ('F', 1)],
    'E': [('G', 19)],
    'F': [('G', 13)],
    'H': [('I', 1), ('J', 2)],
    'I': [('J', 5), ('K', 13), ('G', 5)],
    'J': [('K', 7)],
    'K': [('G', 16)],
    'G': []
}

# Heuristic values
# Values obscured in the screenshot are illustrative
heuristic = {
    'S': 7,
    'A': 8,
    'B': 6,
    'C': 5,
    'D': 6,
    'E': 4,
    'F': 3,
    'H': 7,
    'I': 4,
    'J': 5,
    'K': 3,
    'G': 0
}


def astar(start, goal):

    open_list = []

    heapq.heappush(
        open_list,
        (heuristic[start], 0, start)
    )

    parent = {}
    g_cost = {start: 0}
    visited = set()

    while open_list:

        f, g, current = heapq.heappop(open_list)

        if current in visited:
            continue

        print(
            f"Visited: {current}  "
            f"g={g}  f={f}"
        )

        visited.add(current)

        if current == goal:

            path = []
            cost = g

            while current in parent:
                path.append(current)
                current = parent[current]

            path.append(start)
            path.reverse()

            return path, cost

        for neighbour, edge_cost in graph[current]:

            new_g = g_cost[current] + edge_cost

            if (neighbour not in g_cost
                    or new_g < g_cost[neighbour]):

                g_cost[neighbour] = new_g
                parent[neighbour] = current

                new_f = new_g + heuristic[neighbour]

                heapq.heappush(
                    open_list,
                    (new_f, new_g, neighbour)
                )

    return None, None


start = 'S'
goal = 'G'

print("A* Search\n")

path, cost = astar(start, goal)

if path:
    print("\nOptimal Path")
    print(" -> ".join(path))
    print("\nTotal Cost =", cost)
else:
    print("No Path Found")


# Is A* always the best search algorithm?
print("\nIs A* always the best?")

print(
    "A* is efficient when the heuristic is good "
    "and admissible. However, it is not always "
    "the best for every problem."
)
