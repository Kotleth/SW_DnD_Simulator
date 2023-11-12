import ctypes
from os import getcwd
import numpy as np
new_path = getcwd()
# my_lib = ctypes.CDLL(f'{new_path}/target/release/libtesting.dylib')
my_lib = ctypes.CDLL(f'{new_path}/target/debug/libdnd_lib.dylib')


'''
Rust Wrapper
'''


def testing_func(mat_a):
    my_lib.testing_function.argtypes = [np.ctypeslib.ndpointer(dtype=np.float32), ctypes.c_int, ctypes.c_int]
    my_lib.testing_function.restype = ctypes.POINTER(ctypes.c_float)

    a_matrix = np.array(mat_a, dtype=np.float32)
    print(np.size(a_matrix))
    print(int(np.sqrt(len(a_matrix))))
    result_ptr = my_lib.testing_function(a_matrix, np.size(a_matrix), len(a_matrix))
    result_array = np.ctypeslib.as_array(result_ptr, shape=(np.size(a_matrix),))
    x = result_array.copy()
    my_lib.free(result_ptr)
    return x


matrix = [[2.0, 3.0, 5.0, 6.0], [1.0, 4.0, 6.0, 9.0], [7.0, 8.0, 9.0, 11.0], [3.0, -4.0, 7.0, 13.0]]
print(testing_func(matrix))
