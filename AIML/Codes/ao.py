class AOStar:
    def __init__(self, graph, heuristic):
        self.graph = graph
        self.heuristic = heuristic
        self.status = {}
        self.solution = {}
        self.cost = {}

    def get_neighbors(self, node):
        return self.graph.get(node, [])

    def ao_star(self, node, backtracking=False):
        print("Visiting:", node)
        if node not in self.graph or not self.graph[node]:
            self.status[node] = "Solved"
            return

        min_cost = float("inf")
        best_child = None

        for children in self.graph[node]:
            total_cost = sum(self.heuristic[c] for c in children)
            if total_cost < min_cost:
                min_cost = total_cost
                best_child = children

        self.heuristic[node] = min_cost
        self.solution[node] = best_child

        for child in best_child:
            self.ao_star(child, True)

        if backtracking:
            self.ao_star(node)

    def get_solution(self):
        return self.solution


# Example usage
graph = {
    'A': [['B', 'C'], ['D']],
    'B': [['E', 'F']],
    'C': [],
    'D': [['G', 'H']],
    'E': [],
    'F': [],
    'G': [],
    'H': []
}
heuristic = {'A': 10, 'B': 4, 'C': 2, 'D': 6, 'E': 1, 'F': 1, 'G': 2, 'H': 2}

ao = AOStar(graph, heuristic)
ao.ao_star('A')
print("\nAO* Solution:", ao.get_solution())
