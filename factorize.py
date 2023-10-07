import time
import multiprocessing

def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

# Синхронна версія факторизації
def sync_factorize(numbers):
    results = []
    for number in numbers:
        results.append(factorize(number))
    return results

# Паралельна версія факторизації
def parallel_factorize(numbers):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(factorize, numbers)
    return results


if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060]

    # Виміряйте час виконання для синхронної версії
    start_time = time.time()
    sync_results = sync_factorize(numbers)
    end_time = time.time()
    print(f"Sync Execution Time: {end_time - start_time} seconds")

    # Виміряйте час виконання для паралельної версії
    start_time = time.time()
    parallel_results = parallel_factorize(numbers)
    end_time = time.time()
    print(f"Parallel Execution Time: {end_time - start_time} seconds")

    # Перевірка результатів
    for i in range(len(numbers)):
        assert sync_results[i] == parallel_results[i]
