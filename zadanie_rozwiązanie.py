from utilities import measure_time
from numba import jit, prange
import numpy as np
import random


@measure_time
@jit(nopython=True, parallel=True)   # jit z parallel
def bubble_sort(input_array):
    n = len(input_array)
    for i in prange(n - 1):     # prange zamiast range, aby parallel działał
        for j in prange(n - i - 1):     # prange zamiast range, aby parallel działał
            if input_array[j] > input_array[j + 1]:
                input_array[j], input_array[j + 1] = input_array[j + 1], input_array[j]
    return input_array


if __name__ == "__main__":
    input_array = [random.randint(1, 100) for x in range(10_000)]
    input_array = np.array(input_array)           # Array jak używane z Numba są szybsze niż listy
    bubble_sort(np.zeros(1, input_array.dtype))   # Ważne jest żeby przy pierwszym wywołaniu ustawić dobry typ danych

    print(f"Execution time: {bubble_sort(input_array):.5f}s")