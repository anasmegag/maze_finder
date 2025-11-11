import graph
class Model:
    def __init__(self):
        self.walls = []
        pass
    def get_noeud_number(self,position):
        col_index = position[0] 
        row_index = position[1] 
        
        
        return int(row_index+ col_index/30)

    
    def get_wall(self,positions):
        for position in positions:
            self.walls.append(self.get_noeud_number(position))
        
        return self.walls
    
    def get_graph(self,positions):
        NUMBER_OF_COLUMNS=30
        NUMBER_OF_ROWS = 20
        wall = self.get_wall(positions)
        g = graph.Graph()
        for i in range(NUMBER_OF_ROWS):
            for j in range(NUMBER_OF_COLUMNS):
                if (i*NUMBER_OF_COLUMNS+j) not in wall:
                    if j < NUMBER_OF_COLUMNS -1 and (i*NUMBER_OF_COLUMNS+j+1) not in wall:
                        g.add_arc(i*NUMBER_OF_COLUMNS+j, i*NUMBER_OF_COLUMNS+j+1)
                        g.add_arc(i*NUMBER_OF_COLUMNS+j+1, i*NUMBER_OF_COLUMNS+j)
                    if i < NUMBER_OF_ROWS  and (i*NUMBER_OF_COLUMNS+j+NUMBER_OF_COLUMNS) not in wall:
                        g.add_arc(i*NUMBER_OF_COLUMNS+j, i*NUMBER_OF_COLUMNS+j+NUMBER_OF_COLUMNS)
                        g.add_arc(i*NUMBER_OF_COLUMNS+j+NUMBER_OF_COLUMNS, i*NUMBER_OF_COLUMNS+j)

        return g



