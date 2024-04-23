import time
from typing import List

def factorize(*numbers: int) -> List[List[int]]:
    def get_factors(n: int) -> List[int]:
        return [i for i in range(1, n + 1) if n % i == 0]

    factors = [get_factors(number) for number in numbers]
    for i, number in enumerate(numbers):
        print(f"Фактори числа {number}: {factors[i]}")
    return factors

# Тестові дані
numbers = [128, 255, 99999, 10651060]

# Вимірюємо час виконання
start_time = time.time()
a, b, c, d = factorize(*numbers)
end_time = time.time()

print(f"Час виконання: {end_time - start_time} секунд")
