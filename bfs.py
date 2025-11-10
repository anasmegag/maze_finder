class Graph:
    def __init__(self):
        self.arcs = []

    def add_arc(self, src, dist):
        self.arcs.append((src, dist))

    def get_arcs(self):
        return self.arcs

    def get_all_targets_from_source(self, src):
        targets = []
        for arc in self.arcs:
            if arc[0] == src:
                targets.append(arc[1])
        return targets


class BFS:
    def __init__(self, graph):
        self.graph = graph

    def bfs(self, source):
        visited = {source}
        pred = {source: None}
        queue = [source]

        while queue:
            current_node = queue.pop(0)
            for neighbor in self.graph.get_all_targets_from_source(current_node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    pred[neighbor] = current_node
                    queue.append(neighbor)

        return visited, pred


# --- Example usage ---
g = Graph()
g.add_arc(0, 1)
g.add_arc(1, 2)
g.add_arc(2, 3)
g.add_arc(3, 4)
g.add_arc(1, 4)
g.add_arc(3, 5)
g.add_arc(5, 6)
g.add_arc(3, 6)
g.add_arc(6, 1)

bfs = BFS(g)
visited, pred = bfs.bfs(0)
print("Visited:", visited)
print("Predecessors:", pred)
