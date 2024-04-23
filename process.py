import time
from multiprocessing import Pool, cpu_count, freeze_support
from typing import List

def get_factors(n: int) -> List[int]:
    return [i for i in range(1, n + 1) if n % i == 0]

def factorize(numbers: List[int]) -> List[List[int]]:
    with Pool(cpu_count()) as pool:
        return pool.map(get_factors, numbers)

test_numbers = [128, 255, 99999, 10651060]

if __name__ == '__main__':
    freeze_support()  # This line is necessary for Windows with multiprocessing
    start_time = time.time()
    factors = factorize(test_numbers)
    end_time = time.time()

    for number, number_factors in zip(test_numbers, factors):
        print(f"Фактори числа {number}: {number_factors}")

    print(f"Час виконання: {end_time - start_time} секунд")
    print(f"Кількість ядер процесора: {cpu_count()}")