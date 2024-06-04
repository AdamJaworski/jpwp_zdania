from utilities import measure_time
import random


@measure_time
def bubble_sort(input_array):
    n = len(input_array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if input_array[j] > input_array[j + 1]:
                input_array[j], input_array[j + 1] = input_array[j + 1], input_array[j]
    return input_array


if __name__ == "__main__":
    input_array = [random.randint(1, 100) for x in range(10_000)]
    print(f"Execution time: {bubble_sort(input_array):.5f}s")