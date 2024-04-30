import numpy as np


class MapNoMesh:
    map_matrix = []
    map_dict: dict = {}

    _instance = None

    def __new__(cls, number_of_rows: int, number_of_columns: int):
        if cls._instance is None or ((number_of_rows is not None) and (number_of_columns is not None)):
            cls._instance = super(MapNoMesh, cls).__new__(cls)
            cls.map_matrix = np.ones([50, 50]) * 50
            cls.map_matrix = np.array(cls.map_matrix, dtype=np.int32)
            for row_num, row in enumerate(cls.map_matrix):
                for col_num, value in enumerate(row):
                    cls.map_dict[(row_num, col_num)] = value
        return cls._instance

    # @classmethod
    # def reset_map(cls, number_of_rows: int, number_of_columns: int):
    #     cls.map_matrix = np.ones([number_of_rows, number_of_columns]) * 50
    #     cls.map_matrix = np.array(cls.map_matrix, dtype=np.int32)
    #     for row_num, row in enumerate(cls.map_matrix):
    #         for col_num, value in enumerate(row):
    #             cls.map_dict[(row_num, col_num)] = value

    @classmethod
    def from_matrix(cls, matrix):
        cls.map_matrix = matrix

    def show_map(self):
        print(self.map_matrix)



