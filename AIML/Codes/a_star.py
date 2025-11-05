import heapq

def a_star(graph, start, goal, heuristic):
    pq = [(0, start)]  # (priority, node)
    g_score = {start: 0}
    came_from = {}

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor, cost in graph[current]:
            tentative_g = g_score[current] + cost
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic[neighbor]
                heapq.heappush(pq, (f_score, neighbor))
                came_from[neighbor] = current
    return None


# Example usage
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}

heuristic = {
    'A': 6, 'B': 4, 'C': 5, 'D': 2, 'E': 1, 'F': 0
}

print("\nA* Path:", a_star(graph, 'A', 'F', heuristic))
