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

        return (visited, pred)


