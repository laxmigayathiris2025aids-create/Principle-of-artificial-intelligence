
graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node name: ")

    neighbours = input(
        "Enter neighbours separated by space: "
    ).split()

    graph[node] = neighbours

start = input("Enter start node: ")
goal = input("Enter goal node: ")


def is_valid(node):
    return node in graph


def dfs(current, visited, path):

    if current == goal:
        path.append(current)
        return True

    visited.add(current)

    # Get neighbouring nodes
    neighbours = graph[current]

    for neighbour in neighbours:
        if is_valid(neighbour) and neighbour not in visited:

            if dfs(neighbour, visited, path):
                path.append(current)
                return True

    return False


visited = set()
path = []

if dfs(start, visited, path):

    path.reverse()

    print("\nDFS Path\n")
    print(" -> ".join(path))

    print("\nGraph Representation\n")

    nodes = list(graph.keys())
    size = 3

    for i in range(0, len(nodes), size):
        for node in nodes[i:i + size]:

            if node == start:
                print("S", end="  ")
            elif node == goal:
                print("G", end="  ")
            elif node in path:
                print("*", end="  ")
            else:
                print(".", end="  ")

        print()

else:
    print("No Path Found")
