# Linki #
[Dokumentacja Numba](https://numba.readthedocs.io/en/stable/index.html)

# Opis zadanek #
Celem zadań będzie zoptymalizowanie funkcji znadującej się w [bubble_sort.py](/bubble_sort.py). Kolejne podpunkty będą powoli przyśpieszać funkcję. Do pomiaru czasu używany jest taki sam dekorator jak podczas prezentacji, więc funckja zamiast zwarać tablicę, będzie zwracać czas wykonania.
Domyślnie ustawiłem rozmiar wejściowej listy na 10tys. elementów, u mnie na komputerze wykonanie startowej funckji trwało 4-5 sekund, jeśli dla kogoś będzie to zajmować wiele więcej czasu to można po porstu zmienić ten rozmiar

## Zadanie 1 ##
Korkiem pierwszym będzie dodanie JIT do funkcji. Aby to zrobić wystraczy zaimportować jit z numba oraz dodać dekoraktor @jit do funckji. Ważne jest aby usmieści ten dekoraktor pod @measure_time
```py
from numba import jit
...

@measure_time
@jit()
def bubble_sort(input_array):
...
```
Jako że kompliacja JIT odbywa się przy pierwszym wywołaniu funkcji, dla poprawnych pomiarów musimy wywołać funckję przed wykonaniem pomiaru. Póki co zrobimy to dla jedno elemetnowej listy.
```py
if __name__ == "__main__":
    input_array = [random.randint(1, 100) for x in range(10_000)]
    bubble_sort([0])
    print(f"Execution time: {bubble_sort(input_array):.5f}s")
```
Całość powinna przyśpieszyć funckję ok. 40 krotnie

## Zadanie 2 ##
Drugim krokiem będzie wymiana listy na tablicę. Aby to zrobić najpierw trzeba zaimportować NumPy, a następnie podmienić wcześniej wspomnianą listę.
```py
import numpy as np
...

if __name__ == "__main__":
    input_array = [random.randint(1, 100) for x in range(10_000)]
    input_array = np.array(input_array)
...
```
Dodatkowo teraz trzeba podmienić listę używaną do kompliacji na odpowiadającą danym wejściowym tablicę. Najprosztym sposobem będzie użycie np.zeros:
```py
bubble_sort(np.zeros(1, input_array.dtype))
```
Zamiana listy na tablicę powinna skutkować ok. 2 krotnym przyśpieszeniem

## Zadanie 3 ##
Ostatnim krokiem będzie dodanie wielowątkowości. Aby to zrobić trzeba dodatkowo zaimportować prange z numba, a następnie dodać argumenty nopython i parallel do dekoratora jit i pomienić range na prange. 
```py
from numba import prange
...

@measure_time
@jit(nopython=True, parallel=True)
def bubble_sort(input_array):
    n = len(input_array)
    for i in prange(n - 1):
        for j in prange(n - i - 1):
...
```
Tutaj różnica w prędkości mocno zależy od używanego komputera.
Całość kodu powinna wyglądać tak jak : [zadanie_rozwiązanie.py](/zadanie_rozwiązanie.py)
