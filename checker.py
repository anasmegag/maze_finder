class Predicat:
    def __init__(self):
        pass

    def check_existance(self, ensemble, target):
        return target in ensemble

    def get_way(self, source, target, predecessors, ensemble):
        if not self.check_existance(ensemble, target):
            return None  # Target not reachable

        path = []
        current = target

        while current is not None:
            path.append(current)
            current = predecessors.get(current)

        path.reverse()

        # Check if the path really starts at the source
        if path[0] != source:
            return None  # No valid path

        return path
