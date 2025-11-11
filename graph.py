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

