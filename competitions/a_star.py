""" A simple demonstration of the A* path finding algorithm """
import sys
import heapq

# Read in the 5-word dictionary data
bank = []
with open('data/five_words.txt', 'r') as f:
    for line in f:
        bank += line.split()


def heuristic(curr, goal):
    """ Count word differences to evaluate distance from goal (always overshoot) """
    diff_from_goal = 0  # number of differences from goal
    for i, c in enumerate(curr):
        if i >= len(goal) or c != goal[i]:
            diff_from_goal += 1
    return diff_from_goal


came_from = {}


def a_star(start, end):
    """ Quickly find the shortest path between start and end """
    open_set = []
    heapq.heappush(open_set, (0, start))

    closed_set = set()

    cost_from_start = {bank[i]: sys.maxsize for i in range(len(bank))}
    cost_from_start[start] = 0

    while open_set:
        best_node = heapq.heappop(open_set)[1]
        if best_node == end:
            return True  # found a path

        closed_set.add(best_node)

        # Get neighbors
        for seq in bank:
            if heuristic(seq, best_node) == 1:  # 1 difference, valid neighbor
                if seq in closed_set:
                    continue

                new_cost = cost_from_start[best_node] + 1  # 1 is just a base unit cost
                if new_cost < cost_from_start[seq]:
                    cost_from_start[seq] = new_cost
                    priority = new_cost + heuristic(seq, end)
                    if seq not in open_set:
                        heapq.heappush(open_set, (priority, seq))
                    came_from[seq] = best_node

    return False  # no path found


def build_path(start, goal):
    """ Rebuild the path from start to goal (if exists) """
    current = goal
    path = [current]
    while current != start:
        if current not in came_from:
            return []  # no path exists
        current = came_from[current]
        path.append(current)
    path.append(start)
    path.reverse()
    return path

print("Finding path...")
a_star('money', 'steer')
print(build_path('money', 'steer'))

