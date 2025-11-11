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

        while current !=source:
            path.append(current)
            current = predecessors.get(current)

        path.reverse()
        return path
    
