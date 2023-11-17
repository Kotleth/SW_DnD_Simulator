import ctypes
from os import getcwd
import numpy as np
new_path = getcwd()
# my_lib = ctypes.CDLL(f'{new_path}/target/release/libtesting.dylib')
my_lib = ctypes.CDLL(f'{new_path}/target/release/libdnd_lib.dylib')


'''
Rust Wrapper
'''


def dijkstra_distances(mat_a, starting_point):
    my_lib.dijkstra.argtypes = [np.ctypeslib.ndpointer(dtype=np.float32), ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
    my_lib.dijkstra.restype = ctypes.POINTER(ctypes.c_int)

    a_matrix = np.array(mat_a, dtype=np.float32)

    # I am not really sure how to get anything more than a pointer from Rust to Python without dealing with Cython etc.
    # So this parser needs to stay like this for now
    result_ptr_1 = my_lib.dijkstra(a_matrix, np.size(a_matrix), len(a_matrix), starting_point[0], starting_point[1])
    result_array_1 = np.ctypeslib.as_array(result_ptr_1, shape=(np.size(a_matrix) * 3,))
    distances_array = result_array_1.copy()
    my_lib.free(result_ptr_1)
    distances_dict = {}
    for i in range(int(len(distances_array) / 3)):
        distances_dict[(distances_array[i*2], distances_array[i*2 + 1])] = distances_array[i + int(len(distances_array) * 2 / 3)]
    return distances_dict


matrix = [[50, 100, 50, 50], [50, 50, 50, 50]]
# matrix = [[50.0, 100.0, 50.0, 50.0], [50.0, 50.0, 50.0, 50.0]]
start = (0, 0)
print(testing_func(matrix, start))

