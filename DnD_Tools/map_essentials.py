import numpy as np


class MapNoMesh:
    map_matrix = []

    def __init__(self, number_of_rows: int, number_of_columns: int):
        self.map_matrix = np.ones([number_of_rows, number_of_columns]) * 5
        print(self.map_matrix)


map = MapNoMesh(5, 6)
