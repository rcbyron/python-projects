""" A simple example of a BFS """

# Read in the 5-word dictionary data
bank = []
with open('data/five_words.txt', 'r') as f:
    for line in f:
        bank += line.split()


def bfs(start, goal):
    """ Finds the shortest path between start and goal using BFS """
    queue = [(start, [start])]
    visited = set([start])
    while queue:
        (vertex, path) = queue.pop(0)
        if vertex == goal:
            return path

        for word in bank:
            count = 0
            for i, c in enumerate(vertex):  # Count differences
                if c != word[i]:
                    count += 1
            if count == 1:  # Valid neighbor
                if word not in visited:
                    visited.add(word)
                    queue.append((word, path + [word]))

    return "No path found :("

print("Finding shortest word ladder path...")
print(bfs('money', 'bloop'))
