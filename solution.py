import bfs
import model
import checker

class Solution:
    def __init__(self,positions):
        self.positions=positions
    def getPath(self):
        m = model.Model()
        g= m.get_graph(self.positions)
        parcour = bfs.BFS(g)
        path = parcour.bfs(0)
        check = checker.Predicat()
        solution = check.get_way(0,599,path[1],path[0])
        return solution
        